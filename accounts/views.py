from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Flags
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
import json
# Create your views here.

@csrf_exempt 
def createUser(request):
    json_data = json.loads(request.body)
    newUser = User.objects.create_user(json_data["username"], json_data["email"], json_data["password"])
    profile_data = json_data["profile"]
    newUser.profile.first_name = profile_data["first_name"]
    newUser.profile.last_name = profile_data["last_name"]
    newUser.profile.grade = profile_data["grade"]
    for flag in profile_data["interests"]:
        try:
            flag_value = flag["flag"]
            interest = Flags.objects.get(flag=flag_value)
        except Flags.DoesNotExist:
            interest = Flags.objects.create(**flag)
        newUser.profile.flags.add(interest)
    newUser.save()
    return HttpResponse(status = status.HTTP_201_CREATED)