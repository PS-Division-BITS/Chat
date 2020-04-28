from django.contrib.auth.models import User
from rest_framework import  serializers

from .models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['author', 'content', 'create_date']
