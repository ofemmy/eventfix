from django.contrib import admin
from .models import Ticket, Event, Category
# Register your models here.
admin.site.register((Event, Ticket, Category))
