# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-09 17:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outsource', '0037_order_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='time',
            new_name='get_time',
        ),
    ]
