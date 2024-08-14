from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import *
from .forms import *

# Replace the code in each app below with specific logic as per the app's requirements

@login_required
def cart_detail(request):
    cart = request.user.cart
    return render(request, 'cart/cart_detail.html', {'cart': cart})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart:cart_detail')

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    return redirect('cart:cart_detail')

@login_required
def checkout(request):
    if request.method == 'POST':
        checkout_form = CheckoutForm(request.POST)
        if checkout_form.is_valid():
            # Implement checkout logic here
            return redirect('orders:order_list')
    else:
        checkout_form = CheckoutForm()
    return render(request, 'cart/checkout.html', {'checkout_form': checkout_form})

