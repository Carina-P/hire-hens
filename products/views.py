from django.shortcuts import render

# Create your views here.


def get_products_by_category(request):
    context = {
        "rental": True,
        "category": 'hens',
    }
    return render(request, 'products/products_by_category.html', context)
