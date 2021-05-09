from django.shortcuts import render
from .models import Category

# Create your views here.


def get_products_by_category(request, category, rent_or_buy):
    if rent_or_buy == 'rent':
        rental_categories = Category.objects.filter(rentable=True)
        rent = True
    else:
        rental_categories = []
        rent = False

    context = {
        "rent": rent,
        "this_category": category,
        "rental_categories": rental_categories,
    }
    return render(request, 'products/products_by_category.html', context)
