from django.shortcuts import get_object_or_404
from products.models import Product, Category


def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        product = get_object_or_404(Product, id=item_id)
        category = get_object_or_404(Category, id=product.category.id)
        total += quantity * product.buying_price
        product_count += quantity
        cart_items.append(
            {
                'item_id': item_id,
                'quantity': quantity,
                'product': product,
                'category': category.category
            }
        )

    context = {
        'cart_items': cart_items,
        'total':  total,
        'product_count': product_count
    }

    return context


def cart_rental_contents(request):

    cart_rental_items = []
    total = 0
    product_count = 0
    cart_rental = request.session.get('cart_rental', {})

    for months, info in cart_rental.items():
        for item_id, quantity in info.items():
            product = get_object_or_404(Product, id=item_id)
            category = get_object_or_404(Category, id=product.category.id)
            total += quantity * int(months) * product.rental_price

            product_count += quantity

            cart_rental_items.append(
                {
                    'item_id': item_id,
                    'quantity': quantity,
                    'months': months,
                    'product': product,
                    'category': category.category
                }
            )

    context = {
        'cart_rental_items': cart_rental_items,
        'total_rental':  total,
        'product_rental_count': product_count
    }

    return context
