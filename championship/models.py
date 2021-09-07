from django.db import models

COUNTRY_CHOICES = (
    ('England', 'Англия'),
    ('Spain', 'Испания'),
    ('Germany', 'Гериания'),
    ('Italy', 'Италия'),
    ('France', 'Франция')
)


class League(models.Model):
    title = models.CharField(max_length=50)
    country = models.CharField(max_length=50, choices=COUNTRY_CHOICES)

    def __str__(self):
        return self.title

