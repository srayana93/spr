from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    # Define your URL patterns here
]


urlpatterns += [
    path('', views.order_list, name='order_list'),
    path('<str:order_number>/', views.order_detail, name='order_detail'),
    path('create/', views.order_create, name='order_create'),
    path('update/<str:order_number>/', views.order_update, name='order_update'),
    path('delete/<str:order_number>/', views.order_delete, name='order_delete'),
]

