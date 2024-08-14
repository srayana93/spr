from django.urls import path
from . import views

app_name = 'vendors'

urlpatterns = [
    # Define your URL patterns here
]


urlpatterns += [
    path('dashboard/', views.vendor_dashboard, name='vendor_dashboard'),
    path('products/', views.vendor_product_list, name='vendor_product_list'),
    path('products/create/', views.vendor_product_create, name='vendor_product_create'),
    path('products/update/<slug:slug>/', views.vendor_product_update, name='vendor_product_update'),
    path('products/delete/<slug:slug>/', views.vendor_product_delete, name='vendor_product_delete'),
]

