from django.db.models import fields
from api.models import Category, Event
from rest_framework import serializers
#from api.serializers import EventSerializer
from .models import MyUser as User


class UserEventSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = Event
        fields = ['id', 'name', 'slug', 'description', 'location', 'start_date',
                  'start_time', 'end_date', 'end_time', 'cover_image', 'category']


class UserSerializer(serializers.ModelSerializer):
    events = UserEventSerializer(many=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'events']
