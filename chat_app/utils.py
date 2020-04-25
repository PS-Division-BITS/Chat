from django.conf import settings

import jwt


def decode_jwt(token, secret=settings.SECRET_KEY, algorithms=['HS256',]):
    return jwt.decode(token, secret, algorithms=algorithms)

def verify_token(token, username):
    payload = decode_jwt(token)
    return payload['username'] == username
