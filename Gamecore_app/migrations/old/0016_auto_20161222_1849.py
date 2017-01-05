# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-22 17:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gamecore_app', '0015_auto_20161222_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ladder',
            name='flag_draw',
            field=models.IntegerField(default=0, null=True, verbose_name='Draws'),
        ),
        migrations.AlterField(
            model_name='ladder',
            name='flag_loss',
            field=models.IntegerField(default=0, null=True, verbose_name='Losses'),
        ),
        migrations.AlterField(
            model_name='ladder',
            name='flag_win',
            field=models.IntegerField(default=0, null=True, verbose_name='Winds'),
        ),
        migrations.AlterField(
            model_name='ladder',
            name='goals_received',
            field=models.IntegerField(default=0, null=True, verbose_name='Goals received'),
        ),
        migrations.AlterField(
            model_name='ladder',
            name='goals_scored',
            field=models.IntegerField(default=0, null=True, verbose_name='Goals scored'),
        ),
        migrations.AlterField(
            model_name='ladder',
            name='points',
            field=models.IntegerField(default=0, null=True, verbose_name='Points'),
        ),
        migrations.AlterField(
            model_name='ladder',
            name='shots_target',
            field=models.IntegerField(default=0, null=True, verbose_name='Shots on target'),
        ),
        migrations.AlterField(
            model_name='ladder',
            name='total_shots',
            field=models.IntegerField(default=0, null=True, verbose_name='Total shots'),
        ),
    ]