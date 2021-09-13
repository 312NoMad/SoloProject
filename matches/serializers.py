from rest_framework import serializers

from .models import Matches


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matches
        fields = ('home', 'away', 'status', 'score', 'round', 'league')

    def to_representation(self, instance):
        rep = super(MatchSerializer, self).to_representation(instance)
        rep['league'] = instance.league.title
        return rep
