# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-04 02:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_user', '0007_auto_20190403_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='api_key',
            field=models.CharField(default='a91q96wy5i', editable=False, max_length=10),
        ),
    ]