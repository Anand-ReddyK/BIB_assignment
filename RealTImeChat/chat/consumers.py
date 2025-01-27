import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

# 'online_users' keeps track of all the users in different groups
online_users = {}

class ChatRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'
        self.username = self.scope["user"].username

        # Updating online_users to add new user
        if self.room_group_name not in online_users:
            online_users[self.room_group_name] = set()
        online_users[self.room_group_name].add(self.username)

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

        # When a new user is connected it will notify the group with the updated user list
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'update_users',
                "online_users" : list(online_users[self.room_group_name])
            }
        )

    async def disconnect(self, close_code):

        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        # Updating online_users to remove user
        if self.room_group_name in online_users and self.username in online_users[self.room_group_name]:
            online_users[self.room_group_name].remove(self.username)

            # When a user is disconnected it will notify the group with the updated user list
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'update_users',
                    'online_users': list(online_users[self.room_group_name]),
                }
            )


    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        created_by = text_data_json['created_by']


        message = await self.create_message(message, created_by, self.room_name)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message.content,
                'created_by': message.created_by.username,
                'created_at': message.created_at.strftime("%b. %d, %Y, %I:%M %p"),
            }
        )
    
    # django is trowing django.core.exceptions.ImproperlyConfigured because models are being
    #  - imported before the Django settings are fully loaded, so i am importing them after

    @database_sync_to_async
    def create_message(self, message_content, created_by, room):
        from .models import Messages, ChatRoom, User
        return Messages.objects.create(
            content=message_content,
            created_by=User.objects.get(username=created_by),
            conversation=ChatRoom.objects.get(name=room),
        )


    async def chat_message(self, event):
        message = event['message']
        created_by = event['created_by']
        created_at = event['created_at']
        await self.send(text_data=json.dumps({
            'type': 'chat_message',
            'message': message,
            'created_by': created_by,
            'created_at': created_at,
        }))
    
    async def update_users(self, event):
        online_users = event['online_users']
        await self.send(text_data=json.dumps({
            'type': 'update_users',
            'online_users': online_users,
        }))
