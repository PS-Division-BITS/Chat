from django.contrib.auth import get_user_model
from django.core import serializers

import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # receive message from WebSocket
    def receive(self, text_data=None, bytes_data=None):
        # request from websocket is received here
        text_data_json = json.loads(text_data)
        User = get_user_model()
        sender = serializers.serialize('json', User.objects.filter(id=2))
        sender = list(User.objects.filter(id=2).values('username'))
        message = text_data_json['message']
        # sends out an event to the group having name `self.room_group_name`
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'sender':  sender[0],
                'message': message
            }
        )

    # recieve message from room_group
    def chat_message(self, event):
        sender = event['sender']
        message = event['message']
        print(sender, message)
        # send message back to WebSocket
        self.send(text_data=json.dumps(
            {
                'sender': sender,
                'message': message
            }
        ))
