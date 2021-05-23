from django.shortcuts import (
    render, get_object_or_404, redirect
)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Category, Product
from .forms import ProductForm

# Create your views here.


def get_products_by_category(request, category, rent_or_buy):
    if rent_or_buy == 'rent':
        rental_categories = Category.objects.filter(rentable=True)
        rent = True
    else:
        rental_categories = []
        rent = False

    if category == "all":
        if not request.user.is_superuser:
            messages.error(request, 'Sorry, only store owners can do that.')
            return redirect('home')
        products = Product.objects.all()
    else:
        category_id = get_object_or_404(Category, category=category)
        products = Product.objects.filter(category=category_id.id)

    context = {
        "rent": rent,
        "rent_or_buy": rent_or_buy,
        "this_category": category,
        "rental_categories": rental_categories,
        "products": products
    }
    return render(request, 'products/products_by_category.html', context)


def get_product(request, product_id, rent_or_buy):
    """
    Get information about a product with product_id from database.
    Render the information in product details page.

    Input:
        request (object): The HttpRequest object
        product_id: int, database id of the product
        rent_or_but: str, indicates if it should be rendered on page 
                    for rental or buy
    """
    rent = False
    if rent_or_buy == 'rent':
        rent = True

    product = get_object_or_404(Product, id=product_id)

    context = {
        "product": product,
        "rent": rent,
        "months": request.session.get('months', 1),
    }
    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product. """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect('home')

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, f'Successfully add product: {product.name}!')
            return redirect('get_products_by_category', category='all', rent_or_buy='buy')
        else:
            messages.error(
                request, 'Failed to add product. \
                    Please ensure the form is valid.'
                )
    else:
        form = ProductForm()

    template = 'products/manage_product.html'
    context = {
        'form': form,
        'add': True,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect('home')

    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully updated product: {product.name}!')
            return redirect('get_products_by_category', category='all', rent_or_buy='buy')
        else:
            messages.error(
                request,
                'Failed to update product. Please ensure the form is valid.'
                )
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/manage_product.html'
    context = {
        'form': form,
        'product': product,
        'add': False,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect('home')

    product = get_object_or_404(Product, id=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(
        'get_products_by_category',
        category='all',
        rent_or_buy='buy'
        )
