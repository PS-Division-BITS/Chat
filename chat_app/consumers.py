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
        try:
            # request from websocket is received here
            text_data_json = json.loads(text_data)
            token = text_data_json['token']
            payload = decode_jwt(token)
            sender_qs = User.objects.filter(username=payload['username'])
            message = text_data_json['message']
            # saving msg to database
            new_msg =  Message.objects.create(
                sender=sender_qs[0],
                content=message
            )
            new_msg.chat.add(Chat.objects.get(uri=self.room_name))
            msg_serializer = MessageSerializer(new_msg)
            timestamp = msg_serializer.data['timestamp']
            # sends out an event to the group having name `self.room_group_name`
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'sender':  sender_qs[0].username,
                    'message': message,
                    'timestamp': timestamp
                }
            )
        except Exception as e:
            if settings.DEBUG:
                print(e)
            self.close()

    # recieve message from room_group
    def chat_message(self, event):
        try:
            sender = event['sender']
            # saving the message in Database
            if sender:
                # send message back to WebSocket
                self.send(text_data=json.dumps(
                    {
                        'sender': sender,
                        'message': event['message'],
                        'timestamp': event['timestamp']
                    }
                ))
        except Exception as e:
            if settings.DEBUG:
                print(e)
            self.close()
