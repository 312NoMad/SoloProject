from django.shortcuts import render
from django_filters import rest_framework as filters
from rest_framework import filters as rest_filters
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Player, PlayerStats
from .serializers import PlayerSerializer, PlayerStatsSerializer


class PlayerFilter(filters.FilterSet):
    class Meta:
        model = Player
        fields = ('team', 'national_team')


class PlayerStatsFilter(filters.FilterSet):
    goals_from = filters.NumberFilter('goals', 'gte')
    goals_to = filters.NumberFilter('goals', 'lte')

    games_from = filters.NumberFilter('games', 'gte')
    games_to = filters.NumberFilter('games', 'lte')

    assists_from = filters.NumberFilter('assists', 'gte')
    assists_to = filters.NumberFilter('assists', 'lte')

    class Meta:
        model = PlayerStats
        fields = ('goals_from', 'goals_to', 'games_from', 'games_to', 'assists_from', 'assists_to')


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.DjangoFilterBackend,
                       rest_filters.SearchFilter,
                       rest_filters.OrderingFilter]
    filter_class = PlayerFilter


class PlayerStatsViewSet(viewsets.ModelViewSet):
    queryset = PlayerStats.objects.all()
    serializer_class = PlayerStatsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.DjangoFilterBackend,
                       rest_filters.SearchFilter,
                       rest_filters.OrderingFilter]
    filter_class = PlayerStatsFilter
