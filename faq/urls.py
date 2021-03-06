from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_faq, name='faq'),
    path('add/', views.add_faq, name='add_faq'),
    path('edit/<int:faq_id>', views.edit_faq, name='edit_faq'),
    path('delete/', views.delete_faq, name='delete_faq'),
]
