# Generated by Django 3.2 on 2021-09-08 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('championship', '0002_league_confederation'),
        ('team', '0002_nationalteam_confederation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('released', 'объявлен'), ('going', 'идёт'), ('ended', 'окончен')], default='released', max_length=10)),
                ('score', models.CharField(max_length=8)),
                ('round', models.PositiveSmallIntegerField()),
                ('away', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='away_matches', to='team.team')),
                ('home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_matches', to='team.team')),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='league_matches', to='championship.league')),
            ],
        ),
    ]
