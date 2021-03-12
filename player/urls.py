from django.urls import path, include
from rest_framework import routers
from .views import (
    PlayerListAPIView,
    PlayerCreateAPIView,
    PlayerUpdateAPIView,
    PlayerDestroyAPIView,
)


urlpatterns = [
    path('players/', PlayerListAPIView.as_view(), name='list-players'),
    path('player/add', PlayerCreateAPIView.as_view(), name='create-player'),
    path('player/<pk>/update', PlayerUpdateAPIView.as_view(), name='edit-player'),
    path('player/<pk>/delete', PlayerDestroyAPIView.as_view(), name='delete-player'),
]