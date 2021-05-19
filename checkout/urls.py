from django.urls import path
from . import views
from .webhooks import webhook


urlpatterns = [
    path('', views.checkout, name='checkout'),
    path(
        'checkout_success/<order_number>/',
        views.checkout_success,
        name='checkout_success'
        ),
    path(
        'cache_checkout_data/',
        views.cache_checkout_data,
        name='cache_checkout_data'
        ),
    path('wh/', webhook, name='webhook'),
    path('orders/', views.adm_orders, name='adm_orders'),
    path('deliver_order/<int:order_id>/', views.deliver_order, name='deliver_order'),
]
