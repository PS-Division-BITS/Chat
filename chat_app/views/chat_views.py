from django.conf import settings
from django.contrib.auth import  get_user_model
from django.db.models import Count
from django.utils.datastructures import MultiValueDictKeyError

from rest_framework import permissions, status
from rest_framework.response import  Response
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.views import  APIView
import traceback

from ..models import Chat, Message
from ..serializers import ChatSerializer, MessageSerializer
from ..utils import decode_jwt


User = get_user_model()


class PreloadMessages(APIView):
    "Returns a list of last 50 or less messages"

    throttle_classes = [AnonRateThrottle, UserRateThrottle]

    def get(self, request, format=None):
        try:
            chat = Chat.objects.filter(uri=request.GET['uri'])[0]
        except MultiValueDictKeyError:
            if settings.DEBUG:
                traceback.print_exc()
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
            if settings.DEBUG:
                traceback.print_exc()
            return Response(status=status.HTTP_400_BAD_REQUEST)


class GetChatRooms(APIView):
    "Returns the details of all the rooms the user is part of"

    throttle_classes = [AnonRateThrottle, UserRateThrottle]

    def get(self, request):
        try:
            payload = decode_jwt(request.GET['token'])
            user = User.objects.get(username=payload['username'])
            chats = Chat.objects.filter(participants=user)
            serializer = ChatSerializer(chats, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except MultiValueDictKeyError:
            if settings.DEBUG:
                traceback.print_exc()
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            if settings.DEBUG:
                traceback.print_exc()
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GetAppStats(APIView):
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

    def get(self, request):
        response = {}
        try:
            total_users = User.objects.count()
            total_msgs = Message.objects.count()
            user_with_most_msgs = User.objects.annotate(num_msgs=Count(
                'user_messages'
            )).order_by('-num_msgs', 'id').values('username', 'num_msgs')[:2]
            if str(user_with_most_msgs[0]['username']) == 'Ghost':
                user_with_most_msgs = user_with_most_msgs[1]
            else:
                user_with_most_msgs = user_with_most_msgs[0]
            response['error'] = False
            response['message'] = 'success'
            response['values'] = {
                'totalUsers': total_users,
                'totalMsgs': total_msgs,
                'userWithMostMsgs': str(user_with_most_msgs['username']) + ': ' + str(user_with_most_msgs['num_msgs']),
            }
            response['attrs'] = [
                {'display': 'Total Users', 'prop':'totalUsers'},
                {'display': 'Total Messages sent', 'prop':'totalMsgs'},
                {'display': 'Most Messages', 'prop':'userWithMostMsgs'},
            ]
            return Response(response)
        except Exception:
            if settings.DEBUG:
                traceback.print_exc()
            response['error'] = True
            response['message'] = 'Failed to fetch data'
            return Response(response)
