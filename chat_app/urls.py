from django.urls import path

from .views import auth_views, chat_views


urlpatterns = []

# auth views
urlpatterns += [
    path('auth/login/', auth_views.login_view),
    path('auth/logout/', auth_views.logout_view),
    path('auth/token/verify/', auth_views.verify_token),
]

# chat_views
urlpatterns += [
    path('api/preload/', chat_views.preload_msgs),
]
