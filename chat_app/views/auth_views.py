from django.conf import settings
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.utils.crypto import get_random_string
from django.views.decorators.csrf import csrf_exempt

import jwt

from ..utils import decode_jwt


User = get_user_model()

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        if not User.objects.filter(username=username).exists():
            try:
                password = get_random_string(8)
                User.objects.create_user(
                    username=username,
                    password=password
                )
                # getting the user IP
                x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
                if x_forwarded_for:
                    ip = x_forwarded_for.split(',')[0]
                else:
                    ip = request.META.get('REMOTE_ADDR')
                # creating jwt token
                # the encode() method returns a `byte`, we need to decode
                # it to be able to serialize it
                encoded = jwt.encode({'username': username, 'ip': ip}, settings.SECRET_KEY, algorithm='HS256').decode('utf-8')
                return JsonResponse(
                    {
                        'error': False,
                        'message': 'New user registered',
                        'user': {
                            'username': username,
                            'key': encoded
                        }
                    }, safe=False
                )
            except Exception as e:
                # left for debugging
                print(e)
                return JsonResponse(
                    {
                        'error': True,
                        'message': 'Internal server error'
                    }, safe=False
                )
        else:
            return JsonResponse(
                {
                    'error': True,
                    'message': 'User already exists!'
                }, safe=False
            )

@csrf_exempt
def verify_token(request):
    if request.method == 'POST':
        username = request.POST['username']
        payload = decode_jwt(request.POST['token'])
        if payload['username'] == username:
            return JsonResponse(
                {
                    'verified': True
                }, safe=False
            )
        else:
            return JsonResponse(
                {
                    'verified': False
                }, safe=False
            )

@csrf_exempt
def logout_view(request):
    if request.method == 'POST':
        payload = decode_jwt(request.POST['token'])
        username = payload['username']
        try:
            User.objects.filter(username=username).delete()
            return JsonResponse(
                {
                    'username': username,
                    'error': False,
                    'message': f'{username} successfully un-registered'
                }, safe=False
            )
        except:
            return JsonResponse(
                {
                    'username': username,
                    'error': False,
                    'message': 'Error in deleting username'
                }, safe=False
            )
