# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-05 05:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_user', '0002_auto_20190104_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='api_key',
            field=models.CharField(default='i31r57yb1f', editable=False, max_length=10, unique=True),
        ),
    ]
