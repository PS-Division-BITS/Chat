from django.contrib.auth import get_user_model
from django.db import models

from uuid import uuid4


User = get_user_model()

def deserialize_user(user):
    "Deserialize user model into JSON format"
    return {
        'id': user.id, 'username': user.username, 'email': user.email,
        'name': user.get_full_name()
    }


class TrackableDateModel(models.Model):
    "Abstract model to track creation/update date of a model"
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Message(TrackableDateModel):
    "Model to store messages"
    author = models.ForeignKey(
        User, related_name='user_messages', on_delete=models.CASCADE
    )
    content = models.TextField()
   
    def as_json(self):
        return {
            'author': self.author.username,
            'content': self.content
        }

    def last_50_messages(self):
        return Message.objects.order_by('-create_date').all()[:50]


def _generate_unique_uri():
    "Generate a unique uri for the chat session"
    return str(uuid4()).replace('-', '')[:15]


class Chat(TrackableDateModel):
    "Model for Generic/Group Chat"
    uri = models.URLField(default=_generate_unique_uri)
    message = models.ForeignKey(
        Message, related_name='chat_messages', on_delete=models.DO_NOTHING
    )
    participant = models.ForeignKey(
        User, related_name='user_chats', on_delete=models.CASCADE
    )


class OnetoOneChat(Chat):
    "Proxy model for One to One chat"
    class Meta:
        proxy = True

    def _check_one2one(self):
        if not Chat.objects.values('participant').count() == 2:
            return False
        return True
