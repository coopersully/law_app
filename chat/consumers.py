import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync

from chat.models import Message


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        # Add user to the room
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

        # Fetch last 10 messages from the database
        last_10_messages = reversed(Message.objects.filter(room_name=self.room_name).order_by('-timestamp')[:10])

        for message in last_10_messages:
            await self.send(text_data=json.dumps({
                'message': message.content,
                'author': message.author.username,
                'timestamp': str(message.timestamp)
            }))

    async def disconnect(self, close_code):
        # Remove user from the room
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Store message in the database
        async_to_sync(Message.objects.create)(
            room_name=self.room_name,
            content=message,
            author=self.scope['user']
        )

        # Broadcast message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
