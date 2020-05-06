from django.urls import include, path
from django.conf import  settings

from .views import auth_views, chat_views


urlpatterns = []

# auth endpoints
urlpatterns += [
    path('auth/users/', auth_views.UserRegisterView.as_view()),
    path('auth/login/', auth_views.VerifiedUserLoginView.as_view()),
    path('auth/temp-login/', auth_views.UnverifiedUserLoginView.as_view()),
    path('auth/logout/', auth_views.LogoutView.as_view()),
    path('auth/token/verify/', auth_views.verify_token),
]

# chat/message endpoints
urlpatterns += [
    path('preload/', chat_views.PreloadMessages.as_view()),
    path('user/verify/', chat_views.VerifyUsername.as_view()),
    path('get-rooms/', chat_views.GetChatRooms.as_view()),
    path('get-stats/', chat_views.GetAppStats.as_view()),
]

# only for debugging while using browsable rest-api
if settings.DEBUG:
    urlpatterns += [
        path('api-auth/', include('rest_framework.urls')),
    ]
