from django.contrib.auth import get_user_model
from django.core import serializers

import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    # receive message from WebSocket
    def receive(self, text_data=None, bytes_data=None):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.group_room_name = 'chat_%s' % self.room_name
        text_data_json = json.loads(text_data)
        User = get_user_model()
        sender = serializers.serialize('json', User.objects.filter(id=2))
        message = text_data_json['message']
        # send message to room_group
        async_to_sync(self.channel_layer.group_send)(
            self.group_room_name,
            {
                'type': 'chat_message',
                'sender':  sender,
                'message': message
            }
        )

    # recieve message from room_group
    def chat_message(self, event):
        sender = event['sender']
        message = event['message']
        print(sender, message)
        # send message to WebSocket
        self.send(text_data=json.dumps(
            {
                'sender': sender,
                'message': message
            }
        ))
