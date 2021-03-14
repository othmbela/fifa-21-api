from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
)

from .models import Team
from .serializers import TeamSerializer
from utils.pagination import PaginationPageNumberPagination



class TeamListAPIView(ListAPIView):
    """
    Retrieve FIFA 21 Teams 
    """

    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    pagination_class = PaginationPageNumberPagination



class TeamCreateAPIView(CreateAPIView):
    """
    Create a new FIFA 21 Team
    """

    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamUpdateAPIView(UpdateAPIView):
    """
    Update a FIFA 21 Team
    """

    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamDestroyAPIView(DestroyAPIView):
    """
    Delete a FIFA 21 Team
    """

    queryset = Team.objects.all()
    serializer_class = TeamSerializer