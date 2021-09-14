from rest_framework import generics
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters import rest_framework as filters
from rest_framework import filters as rest_filters

from .models import Matches
from .serializers import MatchSerializer


class MatchFilter(filters.FilterSet):

    class Meta:
        model = Matches
        fields = ('league',)


class MatchViewSet(viewsets.ModelViewSet):
    queryset = Matches.objects.all()
    serializer_class = MatchSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.DjangoFilterBackend,
                       rest_filters.SearchFilter,
                       rest_filters.OrderingFilter]
    filterset_class = MatchFilter


