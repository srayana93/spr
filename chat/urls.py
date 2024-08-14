from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    # Define your URL patterns here
]


urlpatterns += [
    path('', views.chat_window, name='chat_window'),
    path('<int:chat_room_id>/history/', views.chat_history, name='chat_history'),
    path('<int:chat_room_id>/send/', views.send_message, name='send_message'),
]

