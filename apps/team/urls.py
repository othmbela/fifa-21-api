from django.urls import path, include
from rest_framework import routers
from .views import (
    TeamListAPIView,
    TeamCreateAPIView,
    TeamUpdateAPIView,
    TeamDestroyAPIView,
)


urlpatterns = [
    path('teams/', TeamListAPIView.as_view(), name='list-teams'),
    path('team/add', TeamCreateAPIView.as_view(), name='create-team'),
    path('team/<pk>/update', TeamUpdateAPIView.as_view(), name='edit-team'),
    path('team/<pk>/delete', TeamDestroyAPIView.as_view(), name='delete-team'),
]