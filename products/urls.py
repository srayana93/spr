from django.urls import path
from . import views

app_name = 'products'  # This defines the namespace

urlpatterns = [
    # Define your URL patterns here
]


urlpatterns += [
    path('', views.product_list, name='product_list'),
    path('<slug:slug>/', views.product_detail, name='product_detail'),
    path('create/', views.product_create, name='product_create'),
    path('update/<slug:slug>/', views.product_update, name='product_update'),
    path('delete/<slug:slug>/', views.product_delete, name='product_delete'),
    path('bulk-upload/', views.bulk_upload_products, name='bulk_upload_products'),

]

