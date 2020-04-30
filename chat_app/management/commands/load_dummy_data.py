from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

from chat_app.models import *


class Command(BaseCommand):
    def _create(self):
        # creating user and super-user
        User.objects.all().delete()
        print('Creating admin..')
        admin = User.objects.create_user(username='admin', password='qwerty@chat')
        admin.is_superuser = True
        admin.is_staff = True
        admin.save()
        print('admin created.')
        print('username: admin  password: qwerty@chat')

        print('Creating other users..')
        u1 = User.objects.create_user(username='Ritik', password=get_random_string(8))
        u2 = User.objects.create_user(username='Chetan', password=get_random_string(8))
        u3 = User.objects.create_user(username='Random', password=get_random_string(8))
        print('done.')

        # create chats
        Chat.objects.all().delete()
        print('Creating chats..')
        c1 = Chat.objects.create(uri='1', name='main', description='Main Chat Room')
        c2 = Chat.objects.create(uri='2', name='chat2', description='Chat Room 2')
        c3 = Chat.objects.create(uri='3', name='chat3', description='Chat Room 3')
        print('done.')

        # create msgs
        Message.objects.all().delete()
        print('Creating messages..')
        m1 = Message.objects.create(author=admin, content='Hello World!')
        m2 = Message.objects.create(author=admin, content='Foo Bar')
        m3 = Message.objects.create(author=admin, content='Wazz Buzz')
        print('done.')

        # add users to chats
        print('winding up..')
        c1.participants.add(admin, u1, u2, u3)
        c2.participants.add(admin, u1)
        c3.participants.add(admin, u2, u3)

        # add msgs in chats
        c1.messages.add(m1, m2)
        c2.messages.add(m2)
        c3.messages.add(m3)
        print('done.')

    def handle(self, *args, **kwargs):
        self._create()
