# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-07 14:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outsource', '0018_auto_20170807_2226'),
    ]

    operations = [
        migrations.AddField(
            model_name='cafe',
            name='current_order_num',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='order_num',
            field=models.IntegerField(default=0),
        ),
        migrations.RemoveField(
            model_name='event',
            name='beverage',
        ),
        migrations.AddField(
            model_name='event',
            name='beverage',
            field=models.ManyToManyField(blank=True, null=True, related_name='events', to='outsource.Beverage'),
        ),
    ]