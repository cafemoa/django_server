# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-27 17:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outsource', '0027_auto_20170813_2240'),
    ]

    operations = [
        migrations.AddField(
            model_name='beverageoption',
            name='shot_num',
            field=models.IntegerField(default=0),
        ),
    ]
