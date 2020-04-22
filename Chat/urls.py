from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('chat-admin/', admin.site.urls),
    path('chat/', include('chat_app.urls')),
]
