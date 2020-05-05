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

