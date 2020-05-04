from django.urls import re_path

from .consumers import chat_consumer


websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)$', chat_consumer.ChatConsumer),
    re_path(r'ws/chat/(?P<room_name>\w+)/notif/', chat_consumer.ChatConsumer),
]