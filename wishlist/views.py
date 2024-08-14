from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import *
from .forms import *

# Replace the code in each app below with specific logic as per the app's requirements

@login_required
def wishlist_detail(request):
    wishlist = request.user.wishlist
    return render(request, 'wishlist/wishlist_detail.html', {'wishlist': wishlist})

@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist, created = WishList.objects.get_or_create(user=request.user)
    WishListItem.objects.create(wishlist=wishlist, product=product)
    return redirect('wishlist:wishlist_detail')

@login_required
def remove_from_wishlist(request, item_id):
    wishlist_item = get_object_or_404(WishListItem, id=item_id)
    wishlist_item.delete()
    return redirect('wishlist:wishlist_detail')

