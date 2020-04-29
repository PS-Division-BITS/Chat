from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from .models import *


User = get_user_model()


class UserProfileInline(admin.StackedInline):
	model = UserProfile
	can_delete = False
	verbose_name_plural = 'UserProfile'
	fk_name = 'user'


class CustomUserAdmin(UserAdmin):
	inlines = (UserProfileInline,)

	def get_inline_instances(self, request, obj=None):
		if not obj:
			return []
		return super(CustomUserAdmin, self).get_inline_instances(request, obj)
