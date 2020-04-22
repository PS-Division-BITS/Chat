from rest_framework.decorators import api_view
from rest_framework.reverse import  reverse
from rest_framework.views import  APIView
from rest_framework import permissions
from rest_framework.response import  Response

from ..models import Message
from ..serializers import MessageSerializer


class PreloadMessages(APIView):
    "Returns a list of last 50 or less messages"
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        msgs = Message.last_50_messages()
        serializers = MessageSerializer(msgs, many=True)
        return Response(serializers.data)
