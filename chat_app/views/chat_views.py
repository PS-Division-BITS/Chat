from django.conf import settings
from django.contrib.auth import  get_user_model
from django.utils.datastructures import MultiValueDictKeyError

from rest_framework import permissions, status
from rest_framework.response import  Response
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.views import  APIView

from ..models import Chat, Message
from ..permissions import HasValidToken
from ..serializers import ChatSerializer, MessageSerializer
from ..utils import decode_jwt


User = get_user_model()


class PreloadMessages(APIView):
    "Returns a list of last 50 or less messages"

    permission_classes = [HasValidToken, ]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

    def get(self, request, format=None):
        try:
            chat = Chat.objects.filter(uri=request.GET['uri'])[0]
        except MultiValueDictKeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        msgs = chat.get_last_50_messages()
        serializer = MessageSerializer(msgs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class VerifyUsername(APIView):
    "Checks if a username already exists in Database"

    throttle_classes = [AnonRateThrottle, UserRateThrottle]

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

    permission_classes = [HasValidToken, ]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

    def get(self, request):
        try:
            payload = decode_jwt(request.GET['token'])
            user = User.objects.get(username=payload['username'])
            chats = Chat.objects.filter(participants=user)
            serializer = ChatSerializer(chats, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except MultiValueDictKeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            if settings.DEBUG:
                print(e)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
