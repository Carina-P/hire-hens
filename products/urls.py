from django.urls import path
from . import views

urlpatterns = [
    path(
        'products_by_category/<category>/<rent_or_buy>/',
        views.get_products_by_category,
        name='get_products_by_category'
        ),
    path(
        'product_detail/<int:product_id>/<rent_or_buy>/',
        views.get_product,
        name='product_detail'
        ),
    path(
        '<add_product/',
        views.add_product,
        name='add_product'
        ),
    path(
        'edit_product/<int:product_id>/',
        views.edit_product,
        name='edit_product'
        ),
    path(
        'delete_product/<int:product_id>/',
        views.delete_product,
        name='delete_product'
        ),
]
