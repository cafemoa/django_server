# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-25 08:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outsource', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cafe',
            name='orders',
            field=models.ManyToManyField(blank=True, related_name='cafes', to='outsource.Order'),
        ),
        migrations.AlterField(
            model_name='user',
            name='favorite_cafe',
            field=models.ManyToManyField(blank=True, to='outsource.Cafe'),
        ),
    ]
