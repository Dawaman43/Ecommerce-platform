from django import forms
from products.models import Product_Review  # Import from products.models

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Product_Review
        fields = ('rating', 'comment')