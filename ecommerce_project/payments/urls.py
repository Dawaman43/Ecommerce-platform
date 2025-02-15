from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.payment_form, name='payment_form'),
    path('success/', views.payment_success, name='payment_success'),
]