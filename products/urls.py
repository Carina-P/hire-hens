from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_products_by_category, name='get_products_by_category'),
]
