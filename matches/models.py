from django.db import models

from team.models import Team
from championship.models import League


STATUS_CHOICES = (
    ('released', 'объявлен'),
    ('going', 'идёт'),
    ('ended', 'окончен')
)


class Matches(models.Model):
    home = models.ForeignKey(Team,
                             on_delete=models.CASCADE,
                             related_name='home_matches',)
    away = models.ForeignKey(Team,
                             on_delete=models.CASCADE,
                             related_name='away_matches',)

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='released')
    score = models.CharField(max_length=8, blank=True)
    round = models.PositiveSmallIntegerField()
    league = models.ForeignKey(League,
                               on_delete=models.CASCADE,
                               related_name='league_matches')

    def __str__(self):
        return f'{self.home}    :    {self.away}'


