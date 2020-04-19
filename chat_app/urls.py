from django.urls import path

from .views import auth_views


urlpatterns = []

# auth views
urlpatterns += [
    path('auth/login/', auth_views.login_view),
    path('auth/logout/', auth_views.logout_view),
    path('auth/token/verify/', auth_views.verify_token),
]