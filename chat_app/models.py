from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from uuid import uuid4


User = get_user_model()

def get_username(self):
    return self.username

User.add_to_class('__str__', get_username)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = UserProfile()
        user_profile.user = instance
        user_profile.save()
    instance.userprofile.save()


class TrackableDateModel(models.Model):
    "Abstract model to track creation/update date of a model"
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Message(TrackableDateModel):
    "Model to store messages"
    sender = models.ForeignKey(
        User, related_name='user_messages', on_delete=models.DO_NOTHING
    )
    content = models.CharField(max_length=55)


def _generate_unique_uri():
    "Generate a unique uri for the chat session"
    return str(uuid4()).replace('-', '')[:15]


class Chat(TrackableDateModel):
    "Model for Generic/Group Chat"
    uri = models.CharField(
        default=_generate_unique_uri, max_length=20, primary_key=True,
        )
    name = models.CharField(max_length=15)
    description = models.CharField(max_length=50)
    messages = models.ManyToManyField(
        Message, related_name='chat', blank=True,
    )
    participants = models.ManyToManyField(
        User, related_name='user_chats',
    )
    online_participants = models.ManyToManyField(
        User, related_name='user_active_chats',
    )

    def get_last_50_messages(self):
        return Message.objects.filter(chat=self).order_by('create_date')


class OnetoOneChat(Chat):
    "Proxy model for One to One chat"
    class Meta:
        proxy = True

    def _check_one2one(self):
        if not Chat.objects.values('participant').count() == 2:
            return False
        return True
