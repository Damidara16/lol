# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-05 05:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_user', '0004_auto_20190105_0007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='api_key',
            field=models.CharField(default='d31b47qq7s', editable=False, max_length=10, unique=True),
        ),
    ]