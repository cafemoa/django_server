# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-01 08:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outsource', '0011_auto_20170801_1630'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='beverage',
        ),
    ]
