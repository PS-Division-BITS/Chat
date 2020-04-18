from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.utils.crypto import get_random_string


User = get_user_model()

def login_view(request):
    username = request.GET['username']
    if request.method == 'GET':
        print(username)
        if not User.objects.filter(username=username).exists():
            try:
                User.objects.create_user(
                    username=username,
                    password=get_random_string(8)
                )
                print('1')
                return JsonResponse(
                    {
                        'error': False,
                        'message': 'New user registered',
                        'user': {
                            'username': username,
                            'key': username
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
