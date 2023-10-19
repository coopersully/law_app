from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

from chat.models import Message


@login_required
def chat(request):
    context = {
        'page_name': 'chat',
    }
    return render(request, 'chat/index.html', context)


def get_past_messages(request, room_name):
    last_10_messages = Message.objects.filter(room_name=room_name).order_by('-timestamp')[:10]
    messages = [{
        'content': message.content,
        'author': message.author.username,
        'timestamp': str(message.timestamp)
    } for message in reversed(last_10_messages)]

    return JsonResponse({'messages': messages})
