from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from cart.context import cart_contents, cart_rental_contents

import stripe

# Create your views here.


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY


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
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            To the devloper: must be set in the environment.')


    context = {
        'order_form': OrderForm(),
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, 'checkout/checkout.html', context)
