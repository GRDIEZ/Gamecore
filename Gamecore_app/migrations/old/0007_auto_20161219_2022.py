# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-19 19:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gamecore_app', '0006_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='Result',
            field=models.CharField(max_length=120, null=True, verbose_name='Result of the Match'),
        ),
    ]
