from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from orders.models import Order

@login_required
def payment_form(request):
    if request.method == 'POST':
        # Process payment here
        return redirect('payment_success')
    return render(request, 'payments/payment_form.html')

@login_required
def payment_success(request):
    return render(request, 'payments/payment_success.html')