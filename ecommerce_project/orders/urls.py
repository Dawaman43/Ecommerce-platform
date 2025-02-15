from django.urls import path
from . import views

urlpatterns = [
    path('summary/', views.order_summary, name='order_summary'),
    path('shipping-address/', views.shipping_address, name='shipping_address'),
    path('payment/<int:shipping_address_id>/', views.payment, name='payment'),
    path('confirmation/<int:order_id>/', views.order_confirmation, name='order_confirmation'),
    path('history/', views.order_history, name='order_history'),
]