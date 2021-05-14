from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderBuyItem, OrderRentalItem
from products.models import Product
from cart.context import cart_contents, cart_rental_contents

import stripe

# Create your views here.


def checkout(request):
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
            order = order_form.save()
            for item_id, item_data in cart.items():
                try:
                    product = Product.objects.get(id=item_id)
                    order_buy_item = OrderBuyItem(
                        order=order,
                        product=product,
                        quantity=item_data,
                    )
                    order_buy_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag wasn't found in our database. "
                        "Please call us for assistance!")
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
                            months=months,
                        )
                        order_rental_item.save()
                    except Product.DoesNotExist:
                        messages.error(request, (
                            "One of the products in your bag wasn't found in our database. "
                            "Please call us for assistance!")
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
        current_rental_cart = cart_rental_contents(request)
        total_rental = current_rental_cart["total_rental"]
        # Stripe only accepts integer as amount to charge
        stripe_total = round((total + total_rental) * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

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
    Handle sucessful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
            email will be sent to {order.email}.')

    if 'cart' in request.session:
        del request.session['cart']

    if 'cart_rental' in request.session:
        del request.session['cart_rental']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
