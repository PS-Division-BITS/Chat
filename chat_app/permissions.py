from django.conf import settings
from rest_framework import  permissions

from .utils import verify_jwt


class IsNotReservedUserName(permissions.BasePermission):
    message = 'Cannot assign reserved username!'

    def has_permission(self, request, view):
        username = request.GET.get('username') or request.POST.get('username')
        for reserved in settings.RESERVED_USERNAMES:
            if reserved.casefold() == username.casefold():
                return False
        return True


class IsVerifiedUser(permissions.BasePermission):
    message = 'User not registered!'

    def has_obj_permission(self, request, view, obj):
        return obj.is_verifed
