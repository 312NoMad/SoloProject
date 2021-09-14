from rest_framework import serializers

from .models import League
from matches.models import Matches


class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = ('title', 'country', 'confederation')


class LeagueDetailsSerializer(serializers.ModelSerializer):
    league = LeagueSerializer()

    class Meta:
        model = Matches
        fields = ('home', 'away', 'status', 'score', 'round', 'league')
