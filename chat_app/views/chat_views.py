from django.conf import settings
from django.contrib.auth import  get_user_model
from django.utils.datastructures import MultiValueDictKeyError

from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.reverse import  reverse
from rest_framework.views import  APIView
from rest_framework.response import  Response

from ..models import Chat, Message
from ..serializers import ChatSerializer, MessageSerializer
from ..utils import decode_jwt


User = get_user_model()


class PreloadMessages(APIView):
    "Returns a list of last 50 or less messages"
    def get(self, request, format=None):
        try:
            print(request.GET['uri'])
            chat = Chat.objects.filter(uri=request.GET['uri'])
        except MultiValueDictKeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        msgs = chat.get_last_50_messages()
        serializer = MessageSerializer(data=list(msgs), many=True)
        if serializer.is_valid():
            return Response(serializers.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors)


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


class GetChatRooms(APIView):
    "Returns the details of all the rooms the user is part of"
    def get(self, request):
        try:
            payload = decode_jwt(request.GET['token'])
            user = User.objects.get(username=payload['username'])
            chats = Chat.objects.filter(participants=user)
            serializer = ChatSerializer(data=list(chats), many=True)
            if serializer.is_valid():
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors)
        except MultiValueDictKeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            if settings.DEBUG:
                print(e)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
