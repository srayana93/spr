from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'slug', 'created_at', 'updated_at')
    search_fields = ('name', 'slug')
    list_filter = ('parent', 'created_at')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('name',)

