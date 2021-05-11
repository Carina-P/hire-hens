from django.shortcuts import get_object_or_404
from products.models import Product, Category


def rental_package_contents(request):

    package_items = []
    package_total = 0
    package = request.session.get('package', {})

    for item_id, quantity in package.items():
        product = get_object_or_404(Product, id=item_id)
        category = get_object_or_404(Category, id=product.category.id)
        package_total += quantity * product.rental_price

        package_items.append(
            {
                'item_id': item_id,
                'quantity': quantity,
                'product': product,
                'category': category.category
            }
        )

    context = {
        'package_items': package_items,
        'package_total': package_total,
    }

    return context
