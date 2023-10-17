from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def chat(request):
    context = {
        'page_name': 'chat',
    }
    return render(request, 'chat/index.html', context)


@login_required
def chat_room(request, room_name):
    context = {
        'page_name': 'chat',
        'room_name': room_name
    }
    return render(request, 'chat/room.html', context)
