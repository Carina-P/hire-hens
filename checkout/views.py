from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import OrderForm

# Create your views here.


def checkout(request):
    cart = request.session.get('cart', {})
    cart_rental = request.session.get('cart_rental', {})

    if not cart and not cart_rental:
        messages.error(request, "There is nothing in your cart at the moment")
        return redirect('home')

    context = {
        'order_form': OrderForm(),
        'stripe_public_key': 'pk_test_51IX166JKlvgFF1ppZywzGgXRLOalVYSY6XpGTCwLoQx1BJK36QkRFZPzzceMo7noBEjnva5vEQCnz2fP1lCfmulp00Ieu64lFN',
        'client_secret': 'test_client_secret',
    }

    return render(request, 'checkout/checkout.html', context)
