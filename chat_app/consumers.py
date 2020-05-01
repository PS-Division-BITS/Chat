from django.conf import settings
from django.contrib.auth import get_user_model
from django.core import serializers

import json
import jwt
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from .models import Chat, Message
from .utils import decode_jwt


User = get_user_model()


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        if Chat.objects.filter(uri=self.room_name).exists():
            self.room_group_name = 'chat_%s' % self.room_name

            # Join room group
            async_to_sync(self.channel_layer.group_add)(
                self.room_group_name,
                self.channel_name
            )

            self.accept()

    def disconnect(self, close_code):
        # Leave room group
        if hasattr(self, 'room_group_name'):
            async_to_sync(self.channel_layer.group_discard)(
                self.room_group_name,
                self.channel_name
            )

    # receive message from WebSocket
    def receive(self, text_data=None, bytes_data=None):
        # request from websocket is received here
        text_data_json = json.loads(text_data)
        token = text_data_json['token']
        payload = decode_jwt(token)
        sender = User.objects.filter(username=payload['username']).values('username')
        message = text_data_json['message']
        # sends out an event to the group having name `self.room_group_name`
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'sender':  sender[0]['username'],
                'message': message
            }
        )

    # recieve message from room_group
    def chat_message(self, event):
        sender = event['sender']
        message = event['message']
        # saving the message in Database
        author = User.objects.filter(username=sender)
        if author:
            msg = Message.objects.create(
                author=author[0],
                content=message
            )
            # add msg to related chat
            msg.chat.add(Chat.objects.get(uri=self.room_name))
            timestamp = json.dumps(
                msg.create_date, indent=4,sort_keys=True, default=str
            )
            # send message back to WebSocket
            self.send(text_data=json.dumps(
                {
                    'sender': sender,
                    'message': message,
                    'timestamp': timestamp
                }
            ))
        else:
            self.close()
