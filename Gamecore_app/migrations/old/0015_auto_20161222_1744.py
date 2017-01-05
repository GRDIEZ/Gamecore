# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-22 16:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gamecore_app', '0014_ladder'),
    ]

    operations = [
        migrations.AddField(
            model_name='ladder',
            name='flag_draw',
            field=models.FloatField(default=0.0, null=True, verbose_name='Draws'),
        ),
        migrations.AddField(
            model_name='ladder',
            name='flag_loss',
            field=models.FloatField(default=0.0, null=True, verbose_name='Losses'),
        ),
        migrations.AddField(
            model_name='ladder',
            name='flag_win',
            field=models.FloatField(default=0.0, null=True, verbose_name='Winds'),
        ),
        migrations.AddField(
            model_name='ladder',
            name='goals_received',
            field=models.FloatField(default=0.0, null=True, verbose_name='Goals received'),
        ),
        migrations.AddField(
            model_name='ladder',
            name='goals_scored',
            field=models.FloatField(default=0.0, null=True, verbose_name='Goals scored'),
        ),
        migrations.AddField(
            model_name='ladder',
            name='points',
            field=models.FloatField(default=0.0, null=True, verbose_name='Points'),
        ),
        migrations.AddField(
            model_name='ladder',
            name='possesion',
            field=models.FloatField(default=0.0, null=True, verbose_name='possesion'),
        ),
        migrations.AddField(
            model_name='ladder',
            name='shots_target',
            field=models.FloatField(default=0.0, null=True, verbose_name='Shots on target'),
        ),
        migrations.AddField(
            model_name='ladder',
            name='total_shots',
            field=models.FloatField(default=0.0, null=True, verbose_name='Total shots'),
        ),
    ]
