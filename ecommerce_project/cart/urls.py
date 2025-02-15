from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('', views.view_cart, name='cart'),
    path('update/<int:item_id>/', views.update_cart, name='update_cart'),
]