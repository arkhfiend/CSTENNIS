from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
# players/views.py

from rest_framework import viewsets
from .models import Player
from .serializers import PlayerSerializer

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

def ShowHome(request):
    return render(request,"home.html")

def ShowAboutUs(request):
    return render(request,"aboutus.html")

def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")