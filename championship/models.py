from django.db import models

COUNTRY_CHOICES = (
    ('England', 'Англия'),
    ('Spain', 'Испания'),
    ('Germany', 'Гериания'),
    ('Italy', 'Италия'),
    ('France', 'Франция')
)

CONFEDERATIONS_CHOICES = (
    ('UEFA', 'UEFA'),
    ('AFC', 'AFC'),
    ('CAF', 'CAF'),
    ('CONCACAF', 'CONCACAF'),
    ('CONMEBOL', 'CONMEBOL'),
    ('OFC', 'OFC'),
)


class League(models.Model):
    title = models.CharField(max_length=50)
    country = models.CharField(max_length=50, choices=COUNTRY_CHOICES)
    confederation = models.CharField(max_length=10, choices=CONFEDERATIONS_CHOICES)

    def __str__(self):
        return self.title

