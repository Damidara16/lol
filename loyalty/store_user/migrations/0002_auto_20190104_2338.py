# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-05 04:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='api_key',
            field=models.CharField(default='q12d68ou3q', editable=False, max_length=10, unique=True),
        ),
    ]