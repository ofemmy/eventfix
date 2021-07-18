from django.contrib.auth.models import User
from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Event, Category, Ticket
from useraccount.models import MyUser as User
from useraccount.serializers import UserSerializer


def get_category_name(category_data):
    _, category_name = list(category_data.items())[0]
    return category_name


class EventUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class EventSerializer(serializers.ModelSerializer):
    user = EventUserSerializer(read_only=True)
    category = CategorySerializer()

    class Meta:
        model = Event
        fields = ['id', 'name', 'slug', 'description', 'location', 'start_date',
                  'start_time', 'end_date', 'end_time', 'cover_image', 'user', 'category']

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        cat_name = get_category_name(category_data)
        category = Category.objects.get(name=cat_name)
        event = Event.objects.create(**validated_data, category=category)
        return event

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.description = validated_data.get(
            'description', instance.description)
        instance.location = validated_data.get('location', instance.location)
        instance.start_date = validated_data.get(
            'start_date', instance.start_date)
        instance.start_time = validated_data.get(
            'start_time', instance.start_time)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.end_time = validated_data.get('end_time', instance.end_time)
        instance.cover_image = validated_data.get(
            'cover_image', instance.cover_image)
        cat_name = get_category_name(
            validated_data.get('category', instance.category))
        # check if the category changed or not in order to determine whether to fetch from database
        if cat_name != instance.category.name:

            category = Category.objects.get(name=cat_name)
            instance.category = category
        instance.save()
        return instance
