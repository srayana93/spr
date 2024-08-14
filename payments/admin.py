from django.contrib import admin
from .models import *

# Register your models here.


# Add your payment gateway models here if needed

# Example:
# @admin.register(PaymentTransaction)
# class PaymentTransactionAdmin(admin.ModelAdmin):
#     list_display = ('user', 'amount', 'status', 'created_at')
#     search_fields = ('user__email', 'transaction_id')
#     list_filter = ('status', 'created_at')
#     ordering = ('-created_at',)

