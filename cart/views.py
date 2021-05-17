from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

# Create your views here.


def view_cart(request):
    """ A view that renders the cart contents page. """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the product to the shopping cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart

    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """ Adjust the quantity of the specified product to new amount """

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
    else:
        cart.pop(item_id)

    request.session['cart'] = cart
    return redirect('cart')


def remove_from_cart(request, item_id):
    """ Remove item from cart """
    try:
        cart = request.session.get('cart', {})
        cart.pop(item_id)

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, 'Error!:', e)
        return HttpResponse(status=500)


def add_to_cart_rental(request):
    """ Add a rental package to the rental shopping cart """

    months = int(request.POST.get('months'))
    redirect_url = request.POST.get('redirect_url')
    cart_rental = request.session.get('cart_rental', {})
    rental_package = request.session.get('package', {})

    if months in list(cart_rental.keys()):
        for item_id, quantity in rental_package.items():
            if item_id in list(cart_rental[months].keys()):
                cart_rental[months][item_id] += quantity
            else:
                cart_rental[months][item_id] = quantity
    else:
        cart_rental[months] = rental_package

    request.session['cart_rental'] = cart_rental

    if 'package' in request.session:
        del request.session['package']

    return redirect(redirect_url)


def adjust_cart_rental(request, item_id, months):
    """ Adjust the quantity of the specified product to new amount """

    quantity = int(request.POST.get('quantity'))
    cart_rental = request.session.get('cart_rental', {})

    if quantity > 0:
        cart_rental[months][item_id] = quantity
    else:
        if len(cart_rental[months]) == 1:
            cart_rental.pop(months)
        else:
            cart_rental[months].pop(item_id)

    request.session['cart_rental'] = cart_rental
    return redirect('cart')


def remove_from_cart_rental(request, item_id, months):
    """ Remove item from cart """
    try:
        cart_rental = request.session.get('cart_rental', {})
        if len(cart_rental[months]) == 1:
            cart_rental.pop(months)
        else:
            cart_rental[months].pop(item_id)

        request.session['cart_rental'] = cart_rental
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, 'Error!:', e)
        return HttpResponse(status=500)
