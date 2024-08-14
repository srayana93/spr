from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(VendorProfile)
class VendorProfileAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'user', 'business_phone', 'created_at', 'updated_at')
    search_fields = ('company_name', 'user__email')
    list_filter = ('created_at', 'updated_at')
    ordering = ('company_name',)

