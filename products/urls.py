from django.urls import path
from . import views

urlpatterns = [
    path(
        '<category>/<rent_or_buy>',
        views.get_products_by_category,
        name='get_products_by_category'
        ),
    path(
        'product_detail/<product_id>/<rent_or_buy>',
        views.get_product,
        name='product_detail'
        ),
    path('add/<item_id>/', views.add_to_package, name='add_to_package'),
]
