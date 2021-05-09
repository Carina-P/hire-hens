from django.shortcuts import render
from .models import Category, Product

# Create your views here.


def get_products_by_category(request, category, rent_or_buy):
    if rent_or_buy == 'rent':
        rental_categories = Category.objects.filter(rentable=True)
        rent = True
    else:
        rental_categories = []
        rent = False

    category_id = Category.objects.get(category=category)
    products = Product.objects.filter(category=category_id.id)
    print(products)

    context = {
        "rent": rent,
        "this_category": category,
        "rental_categories": rental_categories,
        "products": products
    }
    return render(request, 'products/products_by_category.html', context)
