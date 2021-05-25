from django.shortcuts import (
    render, get_object_or_404, redirect
)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Category, Product
from .forms import ProductForm


def get_products_by_category(request, category, rent_or_buy):
    """
    Get all the products for a special category. I category=all
    all products are fetched.

    Input:
        request (object): The HttpRequest object
        category: str, category for products to fetch
        rent_or_buy: str, Is rent if user wants to rent the products
            and buy if user wants to buy the products.
    """
    if rent_or_buy == 'rent':
        rental_categories = Category.objects.filter(rentable=True)
        rent = True
    else:
        rental_categories = []
        rent = False

    if not category:
        messages.error(
            request, 'Error! Something went wrong. No category given.\
                Contact support!'
            )
        return redirect('home')

    if category == "all":
        if not request.user.is_superuser:
            messages.error(request, 'Sorry, only store owners can do that.')
            return redirect('home')
        try:
            products = Product.objects.all()
        except Exception as e:
            messages.error(
                request,
                "Something went wrong when trying to fetch products\
                from database. Please contact support!", e
            )
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

    if not product_id:
        messages.error(
            request, 'Error! Something went wrong. No product_id given.\
                Contact support!'
            )
        return redirect('home')

    product = get_object_or_404(Product, id=product_id)

    context = {
        "product": product,
        "rent": rent,
        "months": request.session.get('months', 1),
    }
    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """
    Add a new product.
    Render an empty form in manage product.
    When user filled in the form add product to database.
    Only superusers are allowed to do this.

    Input:
        request (object): The HttpRequest object
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect('home')

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(
                request, f'Successfully add product: {product.name}!'
                )
            return redirect(
                'get_products_by_category', category='all', rent_or_buy='buy'
                )
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
    """
    Edit product with product_id.
    Render the form with information about the product to
    be changed.
    When user made changes is form, update product to database.
    Only superusers are allowed to do this.

    Input:
        request (object): The HttpRequest object
        product_id: int, the id of the product in database
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect('home')

    if not product_id:
        messages.error(
            request, 'Error! Something went wrong. No product_id given.\
                Contact support!'
            )
        return redirect('home')

    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Successfully updated product: {product.name}!'
                )
            return redirect(
                'get_products_by_category', category='all', rent_or_buy='buy'
                )
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
    """
    Delete product with product_id.
    Redirect user to the form with all products.
    Only superusers are allowed to do this.

    Input:
        request (object): The HttpRequest object
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect('home')

    if not product_id:
        messages.error(
            request, 'Error! Something went wrong. No product_id given.\
                Contact support!'
            )
        return redirect('home')

    product = get_object_or_404(Product, id=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(
        'get_products_by_category',
        category='all',
        rent_or_buy='buy'
        )
