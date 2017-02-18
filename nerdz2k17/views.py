import json
from django.contrib.auth import authenticate
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from nerdz2k17.models import Profile
from nerdz2k17.serializers import UserSerializer


@csrf_exempt
@api_view(['GET', 'POST', ])
def submit(request):
    if request.method=="POST":
        _email=str(request.POST['email'])
        _event=str(request.POST['event'])
        user=User.objects.get(email=_email)
        User.objects.save()


@csrf_exempt
@api_view(['GET', 'POST', ])
def signup(request):
    if request.method=="POST":
        user=str(request.POST['username'])
        email=str(request.POST['email'])
        password=str(request.POST['password'])
        college=str(request.POST['college'])
        phone=str(request.POST['phone'])
        User.objects.create_user(username=user,email=email,password=password)
        user=User.objects.get(username=user)
        user.profile.college=college
        user.profile.phone=phone
        user.save()

        return HttpResponse("Done")
    return HttpResponse("Error")


@csrf_exempt
@api_view(['GET', 'POST', ])
def loginUser(request):
     if request.method=="POST":
        _user=str(request.POST['username'])
        _password=str(request.POST['password'])
        user=authenticate(username=_user,password=_password)
        if user is not None:
            user=user
            data={'username': user.username, 'college': user.profile.college,'phone':user.profile.phone}
            return HttpResponse(json.dumps(data), content_type='application/json')
        else:
            return HttpResponse("N")




