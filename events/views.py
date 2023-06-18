from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Event
from accounts.models import Flags
from rest_framework import status
import json

# Create your views here.
@csrf_exempt 
def createEvent(request):
    json_data = json.loads(request.body)
    flag_data = json_data.pop("flags")
    newEvent = Event.objects.create(**json_data)
    for element in flag_data:
        try:
            actual_flag = element["flag"]
            flag = Flags.objects.get(flag=actual_flag)
        except Flags.DoesNotExist:
            flag = Flags.objects.create(**element)
        newEvent.flags.add(flag)
    newEvent.save()
    return HttpResponse(status = status.HTTP_201_CREATED)

