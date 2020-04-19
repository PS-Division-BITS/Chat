from django.conf import settings

import jwt


def encode_jwt(payload, secret=settings.SECRET_KEY, algorithm='HS256'):
    jwt.encode({'username': username, 'ip': ip}, settings.SECRET_KEY, algorithm='HS256').decode('utf-8')
    pass

def decode_jwt():
    pass