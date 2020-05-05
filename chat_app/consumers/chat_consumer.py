from django.conf import settings
from django.contrib.auth import get_user_model

import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import traceback

from ..models import Chat, Message
from ..serializers import MessageSerializer
from ..utils import decode_jwt


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
    def receive(self, text_data=None, byte_data=None):
        text_data_json = json.loads(text_data)
        command = text_data_json.get('command', None)
        print(command)
        try:
            token = text_data_json['token']
            payload = decode_jwt(token)
            if command == 'join':
                self.join_room(payload['username'])
            elif command == 'leave':
                self.leave_room(payload['username'])
            elif command == 'send':
                self.send_room(
                    payload['username'], text_data_json['message']
                )
            # elif command = 'list':
            #     self.online_users_list()
        except Exception as e:
            if settings.DEBUG:
                traceback.print_exc()
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
        async_to_sync(self.send(text_data=json.dumps(
                {
                    'error': False,
                    'message': 'success!',
                    'room': self.room_name,
                    'user': new_user
                }
            )))

    def chat_join(self, event):
        "Notify other users"
        async_to_sync(self.send(text_data=json.dumps(
            {
                'msg_type': 'notification',
                'message': f'{event["new_user"]} joined the chat'
            }
        )))

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
        async_to_sync(self.send(text_data=json.dumps(
                {
                    'error': False,
                    'message': 'success!',
                    'room': self.room_name,
                    'user': new_user
                }
            )))

    def chat_leave(self, event):
        "Notify other users"
        async_to_sync(self.send(text_data=json.dumps(
            {
                'msg_type': 'notification',
                'message': f'{event["new_user"]} left the chat'
            }
        )))

    # send messages to users on the group
    def send_room(self, username, message):
        # saving message in DB
        new_msg =  Message.objects.create(
            sender=User.objects.get(username=username),
            content=message
        )
        new_msg.chat.add(self.room)
        msg_serializer = MessageSerializer(new_msg)
        timestamp = msg_serializer.data['timestamp']
        print(username, message, self.room_group_name)
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'sender':  username,
                'message': message,
                'timestamp': timestamp
            }
        )

    def chat_message(self, event):
        "Distribute message to all users in group"
        print('dfdsf', event)
        self.send(text_data=json.dumps(
            {
                'sender': event['sender'],
                'message': event['message'],
                'timestamp': event['timestamp']
            }
        ))
