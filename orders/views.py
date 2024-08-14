from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import *
from .forms import *

# Replace the code in each app below with specific logic as per the app's requirements

@login_required
def order_list(request):
    orders = request.user.orders.all()
    return render(request, 'orders/order_list.html', {'orders': orders})

@login_required
def order_detail(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    return render(request, 'orders/order_detail.html', {'order': order})

@login_required
def order_create(request):
    cart = request.user.cart
    if request.method == 'POST':
        address_form = ShippingAddressForm(request.POST)
        if address_form.is_valid():
            address = address_form.save()
            order = Order.objects.create(user=request.user, total_amount=cart.get_total_price(), shipping_address=address)
            for item in cart.items.all():
                OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity, price=item.price)
            cart.items.all().delete()
            return redirect('orders:order_detail', order_number=order.order_number)
    else:
        address_form = ShippingAddressForm()
    return render(request, 'orders/order_create.html', {'address_form': address_form})

@login_required
def order_update(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    if request.method == 'POST':
        form = OrderUpdateForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('orders:order_detail', order_number=order_number)
    else:
        form = OrderUpdateForm(instance=order)
    return render(request, 'orders/order_update.html', {'form': form})

@login_required
def order_delete(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    if request.method == 'POST':
        order.delete()
        return redirect('orders:order_list')
    return render(request, 'orders/order_delete.html', {'order': order})

