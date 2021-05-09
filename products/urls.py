from django.urls import path
from . import views

urlpatterns = [
    path('<category>/<rent_or_buy>', views.get_products_by_category, name='get_products_by_category'),
]
