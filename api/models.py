from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Ticket(models.Model):
    TICKET_TYPE = [('FREE', 'Free'), ('PAID', 'Paid'),
                   ('INVITE ONLY', 'Invite only')]
    type = models.CharField(max_length=50, choices=TICKET_TYPE, default='FREE')
    name = models.CharField(max_length=50)
    price = models.FloatField(default=0.0),
    max_number = models.IntegerField()
    event = models.ForeignKey("Event", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(
        Category, models.SET_NULL, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateField()
    start_time = models.TimeField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    cover_image = models.TextField(blank=True, null=True)
    user = models.ForeignKey(
        get_user_model(), related_name='events', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
