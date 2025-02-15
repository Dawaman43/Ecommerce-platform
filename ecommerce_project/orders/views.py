from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ShippingAddress, Order, OrderItem
from products.models import Product
from cart.models import Cart, CartItem
from django.core.mail import send_mail

@login_required
def order_summary(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'orders/order_summary.html', {'cart': cart})

@login_required
def shipping_address(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')
        city = request.POST.get('city')
        postal_code = request.POST.get('postal_code')
        country = request.POST.get('country')
        shipping_address = ShippingAddress.objects.create(
            user=request.user,
            first_name=first_name,
            last_name=last_name,
            address=address,
            city=city,
            postal_code=postal_code,
            country=country
        )
        return redirect('payment', shipping_address_id=shipping_address.id)
    return render(request, 'orders/shipping_address.html')

@login_required
def payment(request, shipping_address_id):
    shipping_address = get_object_or_404(ShippingAddress, id=shipping_address_id, user=request.user)
    cart, created = Cart.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        # Here you would integrate with a payment gateway like Stripe
        order = Order.objects.create(user=request.user, shipping_address=shipping_address, paid=True)
        for item in cart.cart_items.all():
            OrderItem.objects.create(order=order, product=item.product, price=item.product.price, quantity=item.quantity)
        # Clear the cart items directly
        CartItem.objects.filter(cart=cart).delete()
        send_mail(
            'Order Confirmation',
            f'Your order has been confirmed.',
            'from@example.com',
            [request.user.email],
            fail_silently=False,
        )
        return redirect('order_confirmation', order_id=order.id)
    return render(request, 'orders/payment.html', {'shipping_address': shipping_address, 'cart': cart})

@login_required
def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'orders/order_confirmation.html', {'order': order})

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/order_history.html', {'orders': orders})