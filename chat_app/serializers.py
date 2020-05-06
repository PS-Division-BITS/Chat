from django.contrib.auth.models import User
from rest_framework import  serializers

from .models import Chat, Message


class MessageSerializer(serializers.ModelSerializer):
    message = serializers.CharField(source='content')
    timestamp = serializers.DateTimeField(source='create_date')

    sender = serializers.SerializerMethodField('get_username')

    class Meta:
        model = Message
        fields = ['sender', 'message', 'timestamp']

    def get_username(self, obj):
        return obj.sender.username


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields =  ['uri', 'name', 'description', 'created_by']
