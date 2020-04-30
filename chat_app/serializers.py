from django.contrib.auth.models import User
from rest_framework import  serializers

from .models import Chat, Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['author', 'content', 'create_date']


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields =  ['uri', 'name', 'description']
