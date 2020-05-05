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


class NotificationConsumer(WebsocketConsumer):
    def connect(self):
        pass
    
    def disconnect(self, close_code):
        pass

    def receive(self, text_data=None, byte_data=None):
        pass
