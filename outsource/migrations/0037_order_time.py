# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-09 17:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outsource', '0036_remove_baseuser_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='time',
            field=models.IntegerField(default=0),
        ),
    ]
