from django.conf import settings
from django.contrib.auth import get_user_model
from django.core import serializers

from rest_framework import serializers

import json
import jwt
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from .models import Chat, Message
from .serializers import MessageSerializer
from .utils import decode_jwt


User = get_user_model()


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        try:
            self.room = Chat.objects.get(uri=self.room_name)
            self.room_group_name = 'chat_%s' % self.room_name
            self.active_rooms = set()
            self.accept()
        except Exception as e:
            if settings.DEBUG:
                print(e)
            self.close()

    def disconnect(self, close_code):
        # Leave room group
        if hasattr(self, 'room_group_name'):
            async_to_sync(self.channel_layer.group_discard)(
                self.room_group_name,
                self.channel_name
            )

    # receives json content from socket
    # text data from json is already decoded here
    def receive_json(self, content):
        command = content.get('command', None)
        print('ass', command)
        try:
            token = content['token']
            payload = decode_jwt(token)
            if command == 'join':
                async_to_sync(self.join_room)(payload['username'])
            elif command == 'leave':
                async_to_sync(self.leave_room)(payload['username'])
            elif command == 'send':
                async_to_sync(self.send_room)(
                    payload['username'], content['message']
                )
        except Exception as e:
            if settings.DEBUG:
                print(e)
            self.close()

    def join_room(self, new_user):
        # Adding user to Chat
        self.room.participants.add(User.objects.get(username=new_user))
        self.active_rooms.add(self.room_name)
        # sending notification to other users
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_join',
                'new_user': new_user
            }
        )
        # adding the user to the group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        # letting client know user has joined
        async_to_sync(self.send_json)(
                {
                    'error': False,
                    'meesage': 'success!',
                    'room': self.room_name,
                    'user': new_user
                }
            )

    def chat_join(self, event):
        "Notify other users"
        async_to_sync(self.send_json)(
            {
                'msg_type': 'notification',
                'message': f'{event["new_user"]} joined the chat'
            }
        )

    def leave_room(self, user):
        # removing user from Chat
        self.room.participants.remove(User.objects.get(username=new_user))
        self.active_rooms.discard(self.room_name)
        # removing the user from the group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_layer
        )
        # sending notification to other users
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_join',
                'new_user': new_user
            }
        )
        # lettings the client know user has left
        async_to_sync(self.send_json)(
                {
                    'error': False,
                    'meesage': 'success!',
                    'room': self.room_name,
                    'user': new_user
                }
            )

    def chat_leave(self, event):
        "Notify other users"
        async_to_sync(self.send_json)(
            {
                'msg_type': 'notification',
                'message': f'{event["new_user"]} left the chat'
            }
        )

    # send messages to users on the group
    def send_room(self, user, meesage):
        # saving message in DB
        new_msg =  Message.objects.create(
            sender=user,
            content=message
        )
        new_msg.chat.add(self.room)
        msg_serializer = MessageSerializer(new_msg)
        timestamp = msg_serializer.data['timestamp']
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'sender':  user,
                'message': message,
                'timestamp': timestamp
            }
        )

    def chat_message(self, event):
        "Distribute message to all users in group"
        self.send(text_data=json.dumps(
            {
                'sender': sender,
                'message': event['message'],
                'timestamp': event['timestamp']
            }
        ))
