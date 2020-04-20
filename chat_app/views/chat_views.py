from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from ..models import Message


@login_required
def preload_msgs(request):
    msgs = Message.last_50_messages()
    msgs_as_json = []
    for msg in msgs:
        msgs_as_json.append(msg.as_json())
    return JsonResponse(
        {
        'msgs': msgs_as_json
        }, safe=False
    )
