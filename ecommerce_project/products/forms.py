from django import forms
from .models import Product, Product_Review

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'stock', 'categories', 'image')

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Product_Review
        fields = ('rating', 'comment')