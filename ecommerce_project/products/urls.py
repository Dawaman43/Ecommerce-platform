from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('product/add/', views.add_product, name='add_product'),
    path('product/<int:id>/edit/', views.edit_product, name='edit_product'),
    path('product/<int:id>/delete/', views.delete_product, name='delete_product'),
]