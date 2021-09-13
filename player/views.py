from django.shortcuts import render
from django_filters import rest_framework as filters
from requests import Response
from rest_framework import filters as rest_filters
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Player, PlayerStats
from .serializers import PlayerSerializer, PlayerStatsSerializer


# class PlayerFilter(filters.FilterSet):
#     age_from = filters.DateFilter('birth_date', 'gte')
#     age_to = filters.DateFilter('birth_date', 'lte')
#
#     class Meta:
#         model = Player
#         fields = ('age_from', 'age_to')


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class PlayerStatsViewSet(viewsets.ModelViewSet):
    queryset = PlayerStats.objects.all()
    serializer_class = PlayerStatsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
