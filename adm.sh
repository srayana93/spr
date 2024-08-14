#!/bin/bash

# Define the apps in your project
APPS=("accounts" "analytics" "cart" "categories" "chat" "orders" "payments" "products" "vendors" "wishlist")

# Function to create and populate admin.py for an app
create_admin_py() {
    local app=$1

    # Create admin.py and populate it with base content
    cat <<EOL > $app/admin.py
from django.contrib import admin
from .models import *

# Register your models here.

EOL
}

# Populate admin.py for each specific app
for app in "${APPS[@]}"; do
    echo "Creating and populating admin.py for $app..."
    create_admin_py $app

    # Specific logic per app
    case $app in
        accounts)
            cat <<EOL >> $app/admin.py

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active')
    search_fields = ('email', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_active')
    ordering = ('email',)

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'city', 'state', 'pincode', 'country')
    search_fields = ('name', 'city', 'state', 'pincode')
    list_filter = ('country',)
    ordering = ('user',)

EOL
            ;;
        analytics)
            cat <<EOL >> $app/admin.py

@admin.register(ProductView)
class ProductViewAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'timestamp')
    search_fields = ('user__email', 'product__name')
    list_filter = ('timestamp',)
    ordering = ('-timestamp',)

@admin.register(OrderAnalytics)
class OrderAnalyticsAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_orders', 'total_spent', 'last_order_date')
    search_fields = ('user__email',)
    list_filter = ('last_order_date',)
    ordering = ('-last_order_date',)

EOL
            ;;
        cart)
            cat <<EOL >> $app/admin.py

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'session_key', 'created_at', 'updated_at')
    search_fields = ('user__email', 'session_key')
    list_filter = ('created_at', 'updated_at')
    ordering = ('-updated_at',)

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity', 'price', 'total_price', 'added_at')
    search_fields = ('cart__user__email', 'product__name')
    list_filter = ('added_at',)
    ordering = ('-added_at',)

EOL
            ;;
        categories)
            cat <<EOL >> $app/admin.py

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'slug', 'created_at', 'updated_at')
    search_fields = ('name', 'slug')
    list_filter = ('parent', 'created_at')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('name',)

EOL
            ;;
        chat)
            cat <<EOL >> $app/admin.py

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'timestamp')
    search_fields = ('sender__email', 'receiver__email')
    list_filter = ('timestamp',)
    ordering = ('-timestamp',)

@admin.register(ChatRoom)
class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at')
    search_fields = ('participants__email',)
    list_filter = ('created_at',)
    ordering = ('-created_at',)

EOL
            ;;
        orders)
            cat <<EOL >> $app/admin.py

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'user', 'status', 'total_amount', 'created_at', 'updated_at')
    search_fields = ('order_number', 'user__email')
    list_filter = ('status', 'created_at', 'updated_at')
    ordering = ('-created_at',)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price')
    search_fields = ('order__order_number', 'product__name')
    ordering = ('order',)

EOL
            ;;
        payments)
            cat <<EOL >> $app/admin.py

# Add your payment gateway models here if needed

# Example:
# @admin.register(PaymentTransaction)
# class PaymentTransactionAdmin(admin.ModelAdmin):
#     list_display = ('user', 'amount', 'status', 'created_at')
#     search_fields = ('user__email', 'transaction_id')
#     list_filter = ('status', 'created_at')
#     ordering = ('-created_at',)

EOL
            ;;
        products)
            cat <<EOL >> $app/admin.py

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'vendor', 'price', 'stock_quantity', 'available', 'created_at', 'updated_at')
    search_fields = ('name', 'vendor__email', 'sku')
    list_filter = ('available', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('name',)

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'image', 'alt_text')
    search_fields = ('product__name',)
    ordering = ('product',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'rating', 'created_at', 'updated_at')
    search_fields = ('product__name', 'user__email')
    list_filter = ('rating', 'created_at', 'updated_at')
    ordering = ('-created_at',)

EOL
            ;;
        vendors)
            cat <<EOL >> $app/admin.py

@admin.register(VendorProfile)
class VendorProfileAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'user', 'business_phone', 'created_at', 'updated_at')
    search_fields = ('company_name', 'user__email')
    list_filter = ('created_at', 'updated_at')
    ordering = ('company_name',)

EOL
            ;;
        wishlist)
            cat <<EOL >> $app/admin.py

@admin.register(WishList)
class WishListAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')
    search_fields = ('user__email',)
    list_filter = ('created_at',)
    ordering = ('-created_at',)

@admin.register(WishListItem)
class WishListItemAdmin(admin.ModelAdmin):
    list_display = ('wishlist', 'product', 'added_at')
    search_fields = ('wishlist__user__email', 'product__name')
    list_filter = ('added_at',)
    ordering = ('-added_at',)

EOL
            ;;
    esac
done

echo "Admin configurations have been created and populated for all apps."
