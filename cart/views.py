from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages


def cart(request):
    """
    Renders the content of the shopping cart.

    Input:
    request (object): The HttpRequest object
    """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """
    Add quantity to the rental shopping cart specified by months and item_id.
    Number of months and quantity is retrieved from form in page.
    Return to url given in form in page.
    Input:
        request (object): The HttpRequest object
        item_id (int): Database id of the product item
    """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    if quantity < 1 or quantity > 40:
        messages.error(
            request,
            "Item is not added you have give an invalid quantity."
            )
        return redirect(redirect_url)

    cart = request.session.get('cart', {})

    # item_str = str(item_id)

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    messages.success(request, "Item was successfully added to cart.")

    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """
    Adjust the buying part of the shopping cart content, in session,
    with the quantity of the specified product to new amount. Quantity
    is retrieved from form in page.
    Redirect user to page with cart information.

    Input:
    request (object): The HttpRequest object
    item_id (int): Database id for a product.
    """

    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})

    if quantity > 0 and quantity < 41:
        cart[item_id] = quantity
    elif quantity == 0:
        cart.pop(item_id)
    else:
        messages.error(
            request,
            "Item is not changed, you have give an invalid quantity."
            )
        return redirect('cart')

    request.session['cart'] = cart
    messages.success(request, "Item in cart was successfully changed.")
    return redirect('cart')


def remove_from_cart(request, item_id):
    """
    Remove item from the buying part of shopping cart

    Input:
    request (object): The HttpRequest object
    item_id (int): Database id for a product.
    """
    try:
        cart = request.session.get('cart', {})
        cart.pop(item_id)

        request.session['cart'] = cart
        messages.success(request, "Item successfully removed from cart.")
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, 'Error!:', e)
        return HttpResponse(status=500)


def add_to_cart_rental(request, item_id):
    """
    Add quantity to the rental shopping cart specified by months and item_id.
    Number of months and quantity is retrieved from form in page.
    Return to url given in form in page.

    Input:
        request (object): The HttpRequest object
        item_id: int, database id of the product item
    """

    months = request.POST.get('months')
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    if int(months) < 1 or int(months) > 40 or quantity < 1 or quantity > 40:
        messages.error(request, "Error: You have given invalid input!")
        return redirect(redirect_url)

    cart_rental = request.session.get('cart_rental', {})

    if months in list(cart_rental.keys()):
        if item_id in list(cart_rental[months].keys()):
            cart_rental[months][item_id] += quantity
        else:
            cart_rental[months][item_id] = quantity
    else:
        cart_rental[months] = {item_id: quantity}

    request.session['cart_rental'] = cart_rental
    request.session['months'] = months
    messages.success(request, "Item was succesfully added to cart.")

    return redirect(redirect_url)


def adjust_cart_rental(request, item_id, months):
    """
    Adjust the rental part of the shopping cart content, in session,
    with the quantity of the specified product and months, to new amount.
    Quantity is retrieved from form in page.
    Redirect user to page with cart content.

    Input:
    request (object): The HttpRequest object
    item_id (int): Database id for a product.
    months (int): Number of months to rent
    """
    quantity = int(request.POST.get('quantity'))
    cart_rental = request.session.get('cart_rental', {})

    if quantity > 0 and quantity < 41 and int(months) > 0 and int(months) < 41:
        cart_rental[months][item_id] = quantity
    elif quantity == 0 and int(months) > 0 and int(months) < 41:
        if len(cart_rental[months]) == 1:
            cart_rental.pop(months)
        else:
            cart_rental[months].pop(item_id)
    else:
        messages.error(
            request, "Nothing was changed. You have given invalid input.")
        return redirect('cart')

    request.session['cart_rental'] = cart_rental
    messages.success(request, "Item was succesfully changed.")
    return redirect('cart')


def remove_from_cart_rental(request, item_id, months):
    """
    Remove item from the buying part of shopping cart

    Input:
    request (object): The HttpRequest object
    item_id (int): Database id for a product.
    """

    try:
        cart_rental = request.session.get('cart_rental', {})
        if len(cart_rental[months]) == 1:
            cart_rental.pop(months)
        else:
            cart_rental[months].pop(item_id)

        request.session['cart_rental'] = cart_rental
        messages.success(request, "Item successfully removed from cart.")
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, 'Error!:', e)
        return HttpResponse(status=500)
