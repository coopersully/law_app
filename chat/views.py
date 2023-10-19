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
        'id': message.id,
        'content': message.content,
        'author': message.author.username,
        'timestamp': str(message.timestamp)
    } for message in reversed(last_10_messages)]

    return JsonResponse({'messages': messages})


@login_required
def register_message(request):
    message_content = request.POST.get('message')
    room_name = request.POST.get('room_name')
    author = request.user

    # Create a new Message object
    new_message = Message.objects.create(
        room_name=room_name,
        author=author,
        content=message_content
    )

    # Save the new Message object to the database
    new_message.save()

    return JsonResponse({'message_id': new_message.id})
