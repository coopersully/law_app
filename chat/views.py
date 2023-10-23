import json

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

from accounts.models import CustomUser
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
        'id': message.id,
        'author': message.author.username,
        'message': message.content,
        'timestamp': str(message.timestamp)
    } for message in reversed(last_10_messages)]

    return JsonResponse({'messages': messages})


@login_required
def register_message(request):
    data = json.loads(request.body.decode('utf-8'))
    message_content = data.get('message')
    room_name = data.get('room_name')
    author = request.user

    print(f'message_content: {message_content}')
    print(f'room_name: {room_name}')

    # Create a new Message object
    new_message = Message.objects.create(
        room_name=room_name,
        author=author,
        content=message_content
    )

    # Save the message to the database
    new_message.save()

    return JsonResponse({'message_id': new_message.id})
