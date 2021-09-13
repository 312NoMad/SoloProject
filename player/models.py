from django.db import models

from team.models import Team, NationalTeam


class Player(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField()
    team = models.ForeignKey(Team,
                             related_name='players',
                             on_delete=models.PROTECT)
    national_team = models.ForeignKey(NationalTeam,
                                      on_delete=models.PROTECT)

    def __str__(self):
        full_name = f'{self.first_name} {self.last_name}'
        return full_name


class PlayerStats(models.Model):
    player = models.ForeignKey(Player,
                               on_delete=models.CASCADE,
                               related_name='statics')
    games = models.PositiveSmallIntegerField()
    goals = models.PositiveSmallIntegerField()
    assists = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.player

