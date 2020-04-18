from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .views import auth_views


urlpatterns = []

# auth views
urlpatterns += [
    path('auth/users/', auth_views.login_view),
]
