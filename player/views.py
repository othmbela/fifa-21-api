from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from rest_framework.response import Response

from .models import Player
from .serializers import PlayerSerializer
from .pagination import PaginationPageNumberPagination


class PlayerListAPIView(ListAPIView):
    """
    Retrieve FIFA 21 Players 
    """

    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    pagination_class = PaginationPageNumberPagination


class PlayerCreateAPIView(CreateAPIView):
    """
    Create a new FIFA 21 Player
    """

    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class PlayerUpdateAPIView(UpdateAPIView):
    """
    Update a FIFA 21 Player
    """

    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class PlayerDestroyAPIView(DestroyAPIView):
    """
    Delete a FIFA 21 Player
    """

    queryset = Player.objects.all()
    serializer_class = PlayerSerializer