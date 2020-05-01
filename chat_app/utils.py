from django.conf import settings
from django.contrib.auth import get_user_model

import jwt


User = get_user_model()


def get_jwt(payload, secret=settings.SECRET_KEY, algorithm='HS256'):
    return jwt.encode(payload, secret, algorithm=algorithm).decode('utf-8')

def decode_jwt(token, secret=settings.SECRET_KEY, algorithms=['HS256',]):
    return jwt.decode(token, secret, algorithms=algorithms)

def verify_jwt(token, username):
    payload = decode_jwt(token)
    return payload['username'] == username

def is_verified_user(user=None, username=None):
    assert user and username is not None
    user = user or User.objects.get(username=username)
    return user.is_verified

def is_reserved_username(username):
    assert username
    for reserved in settings.RESERVED_USERNAMES:
        if reserved.casefold() == username.casefold():
            return True
    return False

def get_ghost_user():
    return User.objects.get(username='Ghost')
