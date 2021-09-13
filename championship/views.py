from django.shortcuts import render
from rest_framework import viewsets
from .models import League
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import LeagueSerializer


class LeagueViewSet(viewsets.ModelViewSet):
    queryset = League.objects.all()
    serializer_class = LeagueSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
