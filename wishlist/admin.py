from django.contrib import admin
from .models import *

# Register your models here.


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

