from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from products.models import Product_Review  # Import from products.models
from products.models import Product
from .forms import ReviewForm

@login_required
def add_review(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            return redirect('product_detail', id=product.id)
    else:
        form = ReviewForm()
    return render(request, 'reviews/review_form.html', {'form': form, 'product': product})