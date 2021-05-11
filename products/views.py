from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product

# Create your views here.


def get_products_by_category(request, category, rent_or_buy):
    if rent_or_buy == 'rent':
        rental_categories = Category.objects.filter(rentable=True)
        rent = True
    else:
        rental_categories = []
        rent = False

    category_id = get_object_or_404(Category, category=category)
    products = Product.objects.filter(category=category_id.id)
    print(products)

    context = {
        "rent": rent,
        "rent_or_buy": rent_or_buy,
        "this_category": category,
        "rental_categories": rental_categories,
        "products": products
    }
    return render(request, 'products/products_by_category.html', context)


def get_product(request, product_id, rent_or_buy):
    rent = False
    if rent_or_buy == 'rent':
        rent = True

    product = get_object_or_404(Product, id=product_id)

    context = {
        "product": product,
        "rent": rent
    }
    return render(request, 'products/product_detail.html', context)


def add_to_package(request, item_id):
    """ Add a quantity of the product to the rental package """

    quantity = int(request.POST.get('quantity'))
    package = request.session.get('package', {})

    if item_id in list(package.keys()):
        package[item_id] += quantity
    else:
        package[item_id] = quantity

    request.session['package'] = package
    product = get_object_or_404(Product, id=item_id)
    category = product.category

    return redirect(
        'get_products_by_category',
        category=category,
        rent_or_buy='rent'
        )
