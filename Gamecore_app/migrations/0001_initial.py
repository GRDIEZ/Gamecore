# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-05 05:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
                ('message', models.CharField(max_length=1200, verbose_name='Message')),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ladder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField(default=0, null=True, verbose_name='Points')),
                ('flag_win', models.IntegerField(default=0, null=True, verbose_name='Winds')),
                ('flag_draw', models.IntegerField(default=0, null=True, verbose_name='Draws')),
                ('flag_loss', models.IntegerField(default=0, null=True, verbose_name='Losses')),
                ('goals_scored', models.IntegerField(default=0, null=True, verbose_name='Goals scored')),
                ('goals_received', models.IntegerField(default=0, null=True, verbose_name='Goals received')),
                ('total_shots', models.IntegerField(default=0, null=True, verbose_name='Total shots')),
                ('shots_target', models.IntegerField(default=0, null=True, verbose_name='Shots on target')),
                ('possession', models.FloatField(default=0.0, null=True, verbose_name='possession')),
            ],
        ),
        migrations.CreateModel(
            name='LogIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(default='', max_length=120)),
                ('password', models.CharField(default='', max_length=120)),
                ('loginTime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeDate', models.CharField(max_length=120, verbose_name='Match date')),
                ('Game', models.CharField(max_length=120, verbose_name='Game')),
                ('Score', models.CharField(max_length=120, null=True, verbose_name='Result of the Match')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('first_name', models.CharField(max_length=120, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=120, verbose_name='Second Name')),
                ('nickname', models.CharField(default='', max_length=120, primary_key=True, serialize=False, verbose_name='Gamecore User Name')),
                ('email', models.CharField(max_length=120, verbose_name='Email')),
                ('telephone', models.CharField(default='', max_length=120, verbose_name='Telephone Number')),
                ('password_first', models.CharField(max_length=120, verbose_name='Password')),
                ('password_second', models.CharField(max_length=120, verbose_name='Password confirmation')),
                ('company', models.CharField(max_length=120, verbose_name='Company Name')),
                ('city', models.CharField(default='', max_length=120, verbose_name='City where you live')),
                ('flag_playstation', models.BooleanField(default=False, verbose_name='Do you play in Playstation?  ')),
                ('flag_xbox', models.BooleanField(default=False, verbose_name='Do you play in Xbox?  ')),
                ('flag_pc', models.BooleanField(default=False, verbose_name='Do you play in PC?  ')),
                ('playstation_id', models.CharField(default='', max_length=120, verbose_name='PlayStation ID')),
                ('welcoming_message', models.CharField(default='Welcome to the game! Tell us your availability and your networking interests and we will set up the right games for you!', max_length=1200)),
                ('available', models.CharField(default='', max_length=300, verbose_name='Update your availability for the next days/weeks')),
            ],
        ),
        migrations.CreateModel(
            name='SuggestedLeague',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.CharField(default='', max_length=120)),
                ('platform', models.CharField(default='', max_length=120)),
                ('time', models.DateTimeField(auto_now=True)),
                ('user_nickname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gamecore_app.Player')),
            ],
        ),
        migrations.AddField(
            model_name='match',
            name='player1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player1', to='Gamecore_app.Player'),
        ),
        migrations.AddField(
            model_name='match',
            name='player2',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='player2', to='Gamecore_app.Player'),
        ),
        migrations.AddField(
            model_name='ladder',
            name='match_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gamecore_app.Match'),
        ),
        migrations.AddField(
            model_name='ladder',
            name='player_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gamecore_app.Player'),
        ),
    ]