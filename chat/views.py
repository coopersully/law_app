from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

from chat.models import Message


@login_required
def chat(request):
    # Get the 'room' query parameter, default to 'public' if not provided
    room = request.GET.get('room', 'public')

    context = {
        'page_name': 'chat',
        'room': room,
    }
    return render(request, 'chat/index.html', context)


@login_required
def get_past_messages(request, room_name):
    last_10_messages = Message.objects.filter(room_name=room_name).order_by('-timestamp')[:10]
    messages = [{
        'id': message.id,
        'author': message.author.username,
        'message': message.content,
        'timestamp': str(message.timestamp)
    } for message in reversed(last_10_messages)]

    return JsonResponse({'messages': messages})
