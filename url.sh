#!/bin/bash

# Define the apps in your project
APPS=("accounts" "analytics" "cart" "categories" "chat" "orders" "payments" "products" "vendors" "wishlist")

# Function to create and populate urls.py for an app
create_urls_py() {
    local app=$1

    # Create urls.py and populate it with base content
    cat <<EOL > $app/urls.py
from django.urls import path
from . import views

app_name = '$app'

urlpatterns = [
    # Define your URL patterns here
]

EOL
}

# Populate urls.py for each specific app
for app in "${APPS[@]}"; do
    echo "Creating and populating urls.py for $app..."
    create_urls_py $app

    # Specific logic per app
    case $app in
        accounts)
            cat <<EOL >> $app/urls.py

urlpatterns += [
    path('profile/', views.profile_view, name='profile'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('password_reset/', views.password_reset_view, name='password_reset'),
    path('password_reset_confirm/<uidb64>/<token>/', views.password_reset_confirm_view, name='password_reset_confirm'),
]

EOL
            ;;
        analytics)
            cat <<EOL >> $app/urls.py

urlpatterns += [
    path('dashboard/', views.analytics_dashboard, name='dashboard'),
    path('reports/', views.report_list, name='report_list'),
    path('report/<int:report_id>/', views.report_detail, name='report_detail'),
    path('report/generate/', views.report_generate, name='report_generate'),
]

EOL
            ;;
        cart)
            cat <<EOL >> $app/urls.py

urlpatterns += [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
]

EOL
            ;;
        categories)
            cat <<EOL >> $app/urls.py

urlpatterns += [
    path('', views.category_list, name='category_list'),
    path('<slug:slug>/', views.category_detail, name='category_detail'),
    path('create/', views.category_create, name='category_create'),
    path('update/<slug:slug>/', views.category_update, name='category_update'),
    path('delete/<slug:slug>/', views.category_delete, name='category_delete'),
]

EOL
            ;;
        chat)
            cat <<EOL >> $app/urls.py

urlpatterns += [
    path('', views.chat_window, name='chat_window'),
    path('<int:chat_room_id>/history/', views.chat_history, name='chat_history'),
    path('<int:chat_room_id>/send/', views.send_message, name='send_message'),
]

EOL
            ;;
        orders)
            cat <<EOL >> $app/urls.py

urlpatterns += [
    path('', views.order_list, name='order_list'),
    path('<str:order_number>/', views.order_detail, name='order_detail'),
    path('create/', views.order_create, name='order_create'),
    path('update/<str:order_number>/', views.order_update, name='order_update'),
    path('delete/<str:order_number>/', views.order_delete, name='order_delete'),
]

EOL
            ;;
        payments)
            cat <<EOL >> $app/urls.py

urlpatterns += [
    path('form/', views.payment_form, name='payment_form'),
    path('success/', views.payment_success, name='payment_success'),
    path('failure/', views.payment_failure, name='payment_failure'),
]

EOL
            ;;
        products)
            cat <<EOL >> $app/urls.py

urlpatterns += [
    path('', views.product_list, name='product_list'),
    path('<slug:slug>/', views.product_detail, name='product_detail'),
    path('create/', views.product_create, name='product_create'),
    path('update/<slug:slug>/', views.product_update, name='product_update'),
    path('delete/<slug:slug>/', views.product_delete, name='product_delete'),
]

EOL
            ;;
        vendors)
            cat <<EOL >> $app/urls.py

urlpatterns += [
    path('dashboard/', views.vendor_dashboard, name='vendor_dashboard'),
    path('products/', views.vendor_product_list, name='vendor_product_list'),
    path('products/create/', views.vendor_product_create, name='vendor_product_create'),
    path('products/update/<slug:slug>/', views.vendor_product_update, name='vendor_product_update'),
    path('products/delete/<slug:slug>/', views.vendor_product_delete, name='vendor_product_delete'),
]

EOL
            ;;
        wishlist)
            cat <<EOL >> $app/urls.py

urlpatterns += [
    path('', views.wishlist_detail, name='wishlist_detail'),
    path('add/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('remove/<int:item_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
]

EOL
            ;;
    esac
done

echo "URL configurations have been created and populated for all apps."
