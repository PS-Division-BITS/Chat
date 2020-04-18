from django.urls import path

from .views import auth_views


urlpatterns = []

# auth views
urlpatterns += [
    path('auth/users/', auth_views.login_view)
]
