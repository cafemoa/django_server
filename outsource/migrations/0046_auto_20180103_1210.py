# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-01-03 12:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outsource', '0045_auto_20180102_1603'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderoptionselector',
            name='option',
        ),
        migrations.AddField(
            model_name='beverageorderoption',
            name='options',
            field=models.ManyToManyField(to='outsource.OrderOptionSelector'),
        ),
    ]