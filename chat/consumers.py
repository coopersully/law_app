import json
from datetime import datetime

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync

from chat.models import Message


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        # Add user to the room
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

        # Fetch the last 10 messages
        last_10_messages = await get_last_10_messages(self.room_name)

        for message in last_10_messages:
            author_username = await get_username_from_message(message)
            await self.send(text_data=json.dumps({
                'message': message.content,
                'author': author_username,
                'timestamp': str(message.timestamp)
            }))

    async def disconnect(self, close_code):
        # Remove user from the room
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Store message in the database
        await database_sync_to_async(Message.objects.create)(
            room_name=self.room_name,
            content=message,
            author=self.scope['user']
        )

        # Broadcast message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'author': self.scope['user'].username,
                'timestamp': str(datetime.now())
            }
        )

    async def chat_message(self, event):
        message = event['message']
        author = event['author']
        timestamp = event['timestamp']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'author': author,
            'timestamp': timestamp
        }))


@database_sync_to_async
def get_last_10_messages(room_name):
    return reversed(Message.objects.filter(room_name=room_name).order_by('-timestamp')[:10])


@database_sync_to_async
def get_username_from_message(message):
    return message.author.username
