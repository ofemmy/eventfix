from api.models import Event
from django.shortcuts import render
from rest_framework import viewsets
from .models import Event
from useraccount.models import MyUser as User
from .serializers import EventSerializer, UserSerializer
# Create your views here.


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
