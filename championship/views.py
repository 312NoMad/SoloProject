from django.shortcuts import render
from rest_framework import viewsets
from django_filters import rest_framework as filters
from rest_framework import filters as rest_filters

from matches.models import Matches
from .models import League
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import LeagueSerializer, LeagueDetailsSerializer


class LeagueFilter(filters.FilterSet):

    class Meta:
        model = League
        fields = ('country', 'confederation')


class LeagueViewSet(viewsets.ModelViewSet):
    queryset = League.objects.all()
    serializer_class = LeagueSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.DjangoFilterBackend,
                       rest_filters.SearchFilter,
                       rest_filters.OrderingFilter]
    filter_class = LeagueFilter


