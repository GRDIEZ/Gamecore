# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-13 03:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Gamecore_app', '0002_auto_20161212_1707'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=120, verbose_name='First name')),
                ('last_name', models.CharField(max_length=120, verbose_name='Last name')),
                ('email', models.CharField(max_length=120, verbose_name='Email address')),
                ('subject', models.CharField(max_length=120, verbose_name='Subject')),
                ('message', models.CharField(max_length=120, verbose_name='Message')),
            ],
        ),
        migrations.CreateModel(
            name='Ladder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField(verbose_name='Position')),
                ('points', models.IntegerField(verbose_name='Points')),
                ('wins', models.IntegerField(verbose_name='Winds')),
                ('draws', models.IntegerField(verbose_name='Draws')),
                ('losses', models.IntegerField(verbose_name='Losses')),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeDate', models.DateField(verbose_name='Match date')),
                ('Game', models.CharField(max_length=120, verbose_name='Game')),
                ('Result', models.CharField(max_length=120, verbose_name='Result of the Match')),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='city',
            field=models.CharField(default='', max_length=120, verbose_name='City where you live'),
        ),
        migrations.AddField(
            model_name='player',
            name='telephone',
            field=models.CharField(default='', max_length=120, verbose_name='Telephone Number'),
        ),
        migrations.AlterField(
            model_name='player',
            name='nickname',
            field=models.CharField(default='', max_length=120, primary_key=True, serialize=False, verbose_name='Gamecore User Name'),
        ),
        migrations.AddField(
            model_name='match',
            name='player1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gamecore_app.Player'),
        ),
        migrations.AddField(
            model_name='ladder',
            name='player_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gamecore_app.Player'),
        ),
    ]
