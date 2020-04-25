from django.urls import include, path
from django.conf import  settings

from .views import auth_views, chat_views


urlpatterns = []

# auth endpoints
urlpatterns += [
    path('temp-auth/login/', auth_views.login_view),
    path('temp-auth/logout/', auth_views.logout_view),
    path('temp-auth/token/verify/', auth_views.verify_token),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]

# chat/message endpoints
urlpatterns += [
    path('preload/', chat_views.PreloadMessages.as_view()),
]

# only for debugging while using browsable rest-api
if settings.DEBUG:
    urlpatterns += [
        path('api-auth/', include('rest_framework.urls'))
    ]
