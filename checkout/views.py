from django.shortcuts import (
    render, redirect, get_object_or_404, reverse, HttpResponse
)
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required

from .forms import OrderForm
from .models import Order, OrderBuyItem, OrderRentalItem

from products.models import Product
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from cart.context import cart_contents, cart_rental_contents

import stripe
import json
from datetime import datetime as date_time
from dateutil.relativedelta import relativedelta
import pytz


@login_required
def adm_orders(request, scope):
    """
    Fetches orders according to scope from database and renders them in
    admin orders page.

    Input:
    request (object): The HttpRequest object
    scope (str): Indicates which orders to show(all, orders not delivered or
    orders with rental due)
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect('home')

    try:
        all_orders = Order.objects.all()

    except Exception as e:
        messages.error(request, 'Something went wrong, fetching orders: ', e)
        return redirect('adm_orders')

    orders = all_orders
    if scope == 'not_delivered':
        # Fetch ealiest end_of_rental date
        orders = all_orders.filter(delivery_date__isnull=True)
    else:
        due_list = []
        for order in orders:
            # Can be different number of rental months with same item.
            earliest_due_date = None
            if order.delivery_date:
                due_dates = OrderRentalItem.objects.filter(
                    order=order.id, end_of_rental__isnull=False,
                    item_returned=False
                    )
                if due_dates:
                    earliest_due_date = (
                        due_dates.earliest('end_of_rental').end_of_rental
                    )
                    due_list.append(order.id)

            order.earliest_due_date = earliest_due_date

    if scope == "due_rentals":
        orders = orders.filter(id__in=due_list)
        # Lose parameters that is not in QuerySet when filter
        # Have to add due dates again
        for order in orders:
            due_dates = OrderRentalItem.objects.filter(
                order=order.id, end_of_rental__isnull=False,
                item_returned=False
                    )
            if due_dates:
                earliest_due_date = (
                    due_dates.earliest('end_of_rental').end_of_rental
                )

            order.earliest_due_date = earliest_due_date

    context = {
        'orders': orders
    }
    return render(request, 'checkout/adm_orders.html', context)


@login_required
def order_details(request, order_id):
    """
    Get order information from database and render in Order detail page

    Input:
    request (object): The HttpRequest object
    order_id (int): The id of the order in database.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect('home')
    
    if not order_id:
        messages.error(request, 'Error! Something went wrong when trying to\
            fetch order. Please contact support!')
        return redirect('home')

    now = date_time.now(pytz.utc)
    context = {
        "order": get_object_or_404(Order, id=order_id),
        "buyitems": OrderBuyItem.objects.filter(order=order_id),
        "rentalitems": OrderRentalItem.objects.filter(order=order_id),
        "now": now
    }
    return render(request, 'checkout/order_details.html', context)


@login_required
def deliver_order(request, order_id):
    """
    Set todays date as delivery date for order with order_id.

    Input:
    request (object): The HttpRequest object
    order_id (int): The id of the order in database.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect('home')

    order = get_object_or_404(Order, id=order_id)

    try:
        order.delivery_date = date_time.now(pytz.utc)
        order.save()

        items = OrderRentalItem.objects.filter(order=order_id)
        for item in items:
            item.end_of_rental = (
                date_time.now(pytz.utc)
                + relativedelta(months=item.months)
                )
            item.save()

        messages.success(
            request, 'Success! Order is updated with today as delivery date'
            )
    except Exception as e:
        messages.error(
            request, 'Something went wrong, setting delivery date: ', e
            )

    return redirect('order_details', order_id)


@login_required
def finish_rental(request, order_id, item_id):
    """
    Rental items is returned and items_returned is set to True for
    item with item_id in the order with order_id.

    Input:
    request (object): The HttpRequest object
    order_id (int): The id of the order in database.
    item_id (int): The id of the item in database.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect('home')

    if not order_id and not item_id:
        messages.error(request, 'Error! Something went wrong when trying to\
            finish rental. Please contact support!')
        return redirect('home')

    item = get_object_or_404(OrderRentalItem, id=item_id)
    print(item)
    try:
        item.item_returned = True
        item.save()
        messages.success(request, 'Success! Rental finished.')
    except Exception as e:
        messages.error(
            request, 'Error! Something went wrong, saving rental finished: ', e
            )

    return redirect('order_details', order_id)


@require_POST
def cache_checkout_data(request):
    """
    From Code institute Boutique Ado.
    Handling the stripe process for payment.

    Input:
    request (object): The HttpRequest object
    """
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'cart_rental': json.dumps(request.session.get('cart_rental', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    """
    This code was highly inspired from Code Institute: Boutique Ado.
    It renders checkout page with form to fill in.
    When user are posting the information. Informationg from form in
    the page are fetched and stripe is contacted for payment.

    Input:
    request (object): The HttpRequest object
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})
        cart_rental = request.session.get('cart_rental', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_cart = json.dumps(cart)
            order.original_cart_rental = json.dumps(cart_rental)
            order.save()

            for item_id, item_data in cart.items():
                try:
                    product = Product.objects.get(id=item_id)
                    order_buy_item = OrderBuyItem(
                        order=order,
                        product=product,
                        quantity=item_data,
                    )
                    order_buy_item.save()
                except Exception as e:
                    messages.error(request, (
                        "Something went wrong when trying to save the order.\
                        Please call us for assistance!", e)
                    )
                    order.delete()
                    return redirect('cart')

            for months, info in cart_rental.items():
                for item_id, quantity in info.items():
                    try:
                        product = Product.objects.get(id=item_id)
                        order_rental_item = OrderRentalItem(
                            order=order,
                            product=product,
                            quantity=quantity,
                            months=int(months),
                        )
                        order_rental_item.save()
                    except Exception as e:
                        messages.error(request, (
                            "Something went wrong when trying to save the order.\
                            Please call us for assistance!", e)
                        )
                        order.delete()
                        return redirect('cart')

            request.session['save_info'] = 'save_info' in request.POST
            return redirect(
                reverse('checkout_success', args=[order.order_number])
                )
        else:
            messages.error(request, 'There was an error with your form\
                Please double check your information')
    else:
        cart = request.session.get('cart', {})
        cart_rental = request.session.get('cart_rental', {})

        if not cart and not cart_rental:
            messages.error(
                request, "There is nothing in your cart at the moment"
                )
            return redirect('home')

        current_cart = cart_contents(request)
        total = current_cart["total"]
        current_cart_rental = cart_rental_contents(request)
        total_rental = current_cart_rental["total_rental"]
        # Stripe only accepts integer as amount to charge
        stripe_total = round((total + total_rental) * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                })
            except Exception:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            To the developer: must be set in the environment.')

    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, 'checkout/checkout.html', context)


def checkout_success(request, order_number):
    """
    This code was highly inspired from Code Institute: Boutique Ado.
    It handles sucessful checkouts and renders the checkout success
    page.

    Input:
    request (object): The HttpRequest object
    order_number (str): The order number of current order.
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        # Save the user's info
        if save_info:
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_country': order.country,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
            email will be sent to {order.email}.')

    if 'cart' in request.session:
        del request.session['cart']

    if 'cart_rental' in request.session:
        del request.session['cart_rental']

    if 'months' in request.session:
        del request.session['months']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
