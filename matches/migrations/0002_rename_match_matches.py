# Generated by Django 3.2 on 2021-09-08 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_nationalteam_confederation'),
        ('championship', '0002_league_confederation'),
        ('matches', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Match',
            new_name='Matches',
        ),
    ]
