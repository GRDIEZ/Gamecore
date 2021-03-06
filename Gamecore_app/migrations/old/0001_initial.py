# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-12 06:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=120)),
                ('last_name', models.CharField(max_length=120)),
                ('email', models.CharField(max_length=120)),
                ('password_first', models.CharField(max_length=120)),
                ('password_second', models.CharField(max_length=120)),
                ('company', models.CharField(max_length=120)),
                ('flag_playstation', models.BooleanField(default=False)),
                ('flag_xbox', models.BooleanField(default=False)),
                ('flag_pc', models.BooleanField(default=False)),
            ],
        ),
    ]
