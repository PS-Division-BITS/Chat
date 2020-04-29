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
	list_display = ('username', 'email', 'first_name', 'last_name', 'get_is_verified')
	list_select_related = ('userprofile',)

	def get_is_verified(self, instance):
		return instance.userprofile.is_verified
	get_is_verified.short_description = 'is_verified'

	def get_inline_instances(self, request, obj=None):
		if not obj:
			return []
		return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Message)
admin.site.register(Chat)
admin.site.register(OnetoOneChat)
