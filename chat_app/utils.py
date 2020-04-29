from django.conf import settings

import jwt


def get_jwt(payload, secret=settings.SECRET_KEY, algorithm='HS256'):
    return jwt.encode(payload, secret, algorithm=algorithm).decode('utf-8')

def decode_jwt(token, secret=settings.SECRET_KEY, algorithms=['HS256',]):
    return jwt.decode(token, secret, algorithms=algorithms)

def verify_jwt(token, username):
    payload = decode_jwt(token)
    return payload['username'] == username
