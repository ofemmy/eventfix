from .views import EventViewSet, UserViewSet
from django.urls import path
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'users', UserViewSet)
urlpatterns = router.urls
