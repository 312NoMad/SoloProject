from rest_framework import serializers

from .models import Player, PlayerStats


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('first_name', 'last_name', 'birth_date', 'team')

    def to_representation(self, instance):
        rep = super(PlayerSerializer, self).to_representation(instance)
        rep['national_team'] = instance.national_team.title
        return rep


class PlayerStatsSerializer(serializers.ModelSerializer):
    player = PlayerSerializer()

    class Meta:
        model = PlayerStats
        fields = ('player', 'games', 'goals', 'assists')

