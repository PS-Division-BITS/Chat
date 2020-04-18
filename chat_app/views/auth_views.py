from django.conf import settings
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.utils.crypto import get_random_string
from django.views.decorators.csrf import csrf_exempt

import jwt


User = get_user_model()

@csrf_exempt
def login_view(request):
    username = request.GET['username']
    if request.method == 'POST':
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
                encoded = jwt.encode({'username': username, 'ip': ip}, settings.SECRET_KEY, algorithm='HS256')
                return JsonResponse(
                    {
                        'error': False,
                        'message': 'New user registered',
                        'user':{
                            'username': username,
                            'key': encoded
                        }
                    }, safe=False
                )
            except:
                print('2')
                return JsonResponse(
                    {
                        'error': True,
                        'message': 'Internal server error'
                    }, safe=False
                )
        else:
            print('3')
            return JsonResponse(
                {
                    'error': True,
                    'message': 'User already exists!'
                }, safe=False
            )
