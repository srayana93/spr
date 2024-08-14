from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import *
from .forms import *

# Replace the code in each app below with specific logic as per the app's requirements

@login_required
def vendor_dashboard(request):
    vendor = request.user.vendor_profile
    products = request.user.vendor_products.all()
    return render(request, 'vendors/vendor_dashboard.html', {'vendor': vendor, 'products': products})

@login_required
def vendor_product_list(request):
    products = request.user.vendor_products.all()
    return render(request, 'vendors/vendor_product_list.html', {'products': products})

@login_required
def vendor_product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.vendor = request.user
            product.save()
            return redirect('vendors:vendor_product_list')
    else:
        form = ProductForm()
    return render(request, 'vendors/vendor_product_create.html', {'form': form})

@login_required
def vendor_product_update(request, slug):
    product = get_object_or_404(Product, slug=slug)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('vendors:vendor_product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'vendors/vendor_product_update.html', {'form': form})

@login_required
def vendor_product_delete(request, slug):
    product = get_object_or_404(Product, slug=slug)
    if request.method == 'POST':
        product.delete()
        return redirect('vendors:vendor_product_list')
    return render(request, 'vendors/vendor_product_delete.html', {'product': product})

