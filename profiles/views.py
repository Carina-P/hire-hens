from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order


@login_required
def profile(request):
    """
    Display the user's profile.
    Input:
        request (object): The HttpRequest object
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(
                request, 'Update failed. Please ensure the form is valid.'
                )
    else:
        form = UserProfileForm(instance=profile)

    try:
        orders = profile.orders.all()
    except Exception as e:
        messages.error(request, "Something went wrong trying to fetch order \
            information from database. Contact support!", e)

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, template, context)


def order_history(request, order_number):
    """
    Fetches order history and renders in checkout page.

    Input:
        request (object): The HttpRequest object
        order_number (str): Ordernumber

    """

    if order_number:
        order = get_object_or_404(Order, order_number=order_number)
    else:
        messages.error(request, "Something is wrong with ordernumber.\
            Please contact support!")

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
