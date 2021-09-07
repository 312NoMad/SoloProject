from django.db import models

from championship.models import League

COUNTRY_CHOICES = (
    ('England', 'Англия'),
    ('Spain', 'Испания'),
    ('Germany', 'Германия'),
    ('France', 'Франция'),
    ('Italy', 'Италия'),
    ('Argentina', 'Аргентина'),
    ('Brazil', 'Бразилия'),
    ('Belgium', 'Бельгия'),
    ('Croatia', 'Хорватия'),
    ('Sweden', 'Швеция'),
    ('Portugal', 'Португалия'),
)

CONFEDERATIONS_CHOICES = (
    ('UEFA', 'UEFA'),
    ('AFC', 'AFC'),
    ('CAF', 'CAF'),
    ('CONCACAF', 'CONCACAF'),
    ('CONMEBOL', 'CONMEBOL'),
    ('OFC', 'OFC'),
)


class Team(models.Model):
    title = models.CharField(max_length=50, primary_key=True)
    league = models.ForeignKey(League,
                               related_name='teams',
                               on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class NationalTeam(models.Model):
    title = models.CharField(max_length=50, choices=COUNTRY_CHOICES)
    confederation = models.CharField(max_length=10, choices=CONFEDERATIONS_CHOICES)

    def __str__(self):
        return self.title


# class LineUp(models.Model):
#     goalkeepers =
#     defenders =
#     middlefielders =
#     forwards =
#
