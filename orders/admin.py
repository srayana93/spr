from django.contrib import admin
from .models import *

# Register your models here.


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

