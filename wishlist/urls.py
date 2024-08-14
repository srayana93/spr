from django.urls import path
from . import views

app_name = 'wishlist'

urlpatterns = [
    # Define your URL patterns here
]


urlpatterns += [
    path('', views.wishlist_detail, name='wishlist_detail'),
    path('add/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('remove/<int:item_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
]

