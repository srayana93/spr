from django.contrib import admin
from .models import *

# Register your models here.


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

