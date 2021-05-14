from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from cart.context import cart_contents, cart_rental_contents

import stripe

# Create your views here.


def checkout(request):
    cart = request.session.get('cart', {})
    cart_rental = request.session.get('cart_rental', {})

    if not cart and not cart_rental:
        messages.error(request, "There is nothing in your cart at the moment")
        return redirect('home')

    current_cart = cart_contents(request)
    total = current_cart["total"]
    current_rental_cart = cart_rental_contents(request)
    total_rental = current_rental_cart["total_rental"]
    # Stripe only accepts integer as amount to charge
    stripe_total = round((total + total_rental) * 100)

    context = {
        'order_form': OrderForm(),
        'stripe_public_key': 'pk_test_51IX166JKlvgFF1ppZywzGgXRLOalVYSY6XpGTCwLoQx1BJK36QkRFZPzzceMo7noBEjnva5vEQCnz2fP1lCfmulp00Ieu64lFN',
        'client_secret': 'test_client_secret',
    }

    return render(request, 'checkout/checkout.html', context)
