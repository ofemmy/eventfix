from django.contrib.auth.models import User
from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Event, Category, Ticket
from useraccount.models import MyUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['id', 'email', 'first_name', 'last_name']


class EventSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    category = serializers.StringRelatedField()

    class Meta:
        model = Event
        fields = ['id', 'name', 'slug', 'description', 'location', 'start_date',
                  'start_time', 'end_date', 'end_time', 'cover_image', 'user', 'category']
