# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-01 07:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('outsource', '0010_auto_20170801_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='beverage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events', to='outsource.Beverage'),
        ),
    ]
