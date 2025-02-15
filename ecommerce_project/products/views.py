from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product, Product_Review, Category
from .forms import ProductForm, ReviewForm
from django.contrib import messages

def product_list(request):
    products = Product.objects.filter(available=True)
    categories = Category.objects.all()
    category_id = request.GET.get('category_id')
    if category_id:
        products = products.filter(categories__id=category_id)
    return render(request, 'products/product_list.html', {'products': products, 'categories': categories, 'category_id': category_id})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id, available=True)
    reviews = product.product_reviews.all()
    return render(request, 'products/product_detail.html', {'product': product, 'reviews': reviews})

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user
            product.save()
            form.save_m2m()
            messages.success(request, 'Product added successfully.')
            return redirect('product_detail', id=product.id)
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = ProductForm()
    return render(request, 'products/add_product.html', {'form': form})

@login_required
def edit_product(request, id):
    product = get_object_or_404(Product, id=id, seller=request.user)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully.')
            return redirect('product_detail', id=product.id)
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/edit_product.html', {'form': form})

@login_required
def delete_product(request, id):
    product = get_object_or_404(Product, id=id, seller=request.user)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted successfully.')
        return redirect('product_list')
    return render(request, 'products/delete_product.html', {'product': product})

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
            messages.success(request, 'Review added successfully.')
            return redirect('product_detail', id=product.id)
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = ReviewForm()
    return render(request, 'reviews/review_form.html', {'form': form, 'product': product})