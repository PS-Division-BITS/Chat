from rest_framework import  permissions

from .utils import verify_jwt


class HasValidToken(permissions.BasePermission):
    def has_object_permssion(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        verify_jwt(request.POST['token'], request.user.username)
