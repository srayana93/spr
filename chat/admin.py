from django.contrib import admin
from .models import *

# Register your models here.


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

