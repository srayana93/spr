from django.contrib import admin
from .models import *

# Register your models here.


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

