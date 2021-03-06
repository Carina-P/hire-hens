from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('add/<item_id>/', views.add_to_cart, name='add_to_cart'),
    path('adjust/<item_id>/', views.adjust_cart, name='adjust_cart'),
    path(
        'remove/',
        views.remove_from_cart,
        name='remove_from_cart'
        ),
    path(
        'add_rental/<item_id>/',
        views.add_to_cart_rental,
        name='add_to_cart_rental'),
    path(
        'adjust_rental/<item_id>/<months>/',
        views.adjust_cart_rental,
        name='adjust_cart_rental'
        ),
    path(
        'remove_rental/',
        views.remove_from_cart_rental,
        name='remove_from_cart_rental'
        ),
]
