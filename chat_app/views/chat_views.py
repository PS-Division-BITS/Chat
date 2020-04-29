from django.contrib.auth import  get_user_model
from django.utils.datastructures import MultiValueDictKeyError

from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.reverse import  reverse
from rest_framework.views import  APIView
from rest_framework.response import  Response

from ..models import Message
from ..serializers import MessageSerializer


User = get_user_model()


class PreloadMessages(APIView):
    "Returns a list of last 50 or less messages"
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        msgs = Message.last_50_messages()
        serializers = MessageSerializer(msgs, many=True)
        return Response(serializers.data)


class VerifyUsername(APIView):
    "Checks if a username already exists in Database"
    def get(self, request):
        try:
            verified = User.objects.filter(
                username=request.GET['username']
            ).exists()
            return Response(
                data={'verified': verified},
                status=status.HTTP_200_OK
            )
        except MultiValueDictKeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
