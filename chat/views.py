from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import *
from .forms import *

# Replace the code in each app below with specific logic as per the app's requirements

@login_required
def chat_window(request):
    chat_rooms = request.user.chat_rooms.all()
    return render(request, 'chat/chat_window.html', {'chat_rooms': chat_rooms})

@login_required
def chat_history(request, chat_room_id):
    chat_room = get_object_or_404(ChatRoom, id=chat_room_id)
    messages = chat_room.messages.all()
    return render(request, 'chat/chat_history.html', {'chat_room': chat_room, 'messages': messages})

@login_required
def send_message(request, chat_room_id):
    chat_room = get_object_or_404(ChatRoom, id=chat_room_id)
    if request.method == 'POST':
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            chat_message = form.save(commit=False)
            chat_message.sender = request.user
            chat_message.receiver = chat_room.participants.exclude(id=request.user.id).first()
            chat_message.save()
            return redirect('chat:chat_history', chat_room_id=chat_room_id)
    else:
        form = ChatMessageForm()
    return render(request, 'chat/send_message.html', {'form': form, 'chat_room': chat_room})

