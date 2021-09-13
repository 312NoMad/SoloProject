from rest_framework import serializers

from .models import Player, PlayerStats


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('first_name', 'last_name', 'team')


class PlayerStatsSerializer(serializers.ModelSerializer):
    player = PlayerSerializer()

    class Meta:
        model = PlayerStats
        fields = ('player', 'games', 'goals', 'assists')

