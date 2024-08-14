from django.contrib import admin
from .models import *

# Register your models here.


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

