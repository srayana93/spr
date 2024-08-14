from django.contrib import admin
from .models import *

# Register your models here.


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

