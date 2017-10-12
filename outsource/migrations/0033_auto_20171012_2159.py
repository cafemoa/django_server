# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-12 21:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outsource', '0032_alert'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='birth_day',
        ),
        migrations.RemoveField(
            model_name='user',
            name='birth_month',
        ),
        migrations.RemoveField(
            model_name='user',
            name='birth_year',
        ),
        migrations.AddField(
            model_name='user',
            name='birth',
            field=models.IntegerField(default=980818),
        ),
    ]