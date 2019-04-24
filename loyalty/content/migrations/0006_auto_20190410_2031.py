# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-11 00:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store_user', '0009_auto_20190410_2031'),
        ('content', '0005_auto_20190403_2206'),
    ]

    operations = [
        migrations.CreateModel(
            name='cartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemCount', models.PositiveIntegerField(default=0)),
                ('item', models.ManyToManyField(to='content.Item')),
            ],
        ),
        migrations.CreateModel(
            name='CartItemNumOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('maxQuanity', models.PositiveIntegerField(default=10)),
                ('minQuanity', models.PositiveIntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, max_digits=3)),
                ('applied', models.BooleanField(default=False)),
                ('applications_amount', models.PositiveIntegerField(default=0)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_user.Store')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CartItemSelectOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=3)),
                ('applied', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ItemNumOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('maxQuanity', models.PositiveIntegerField(default=10)),
                ('minQuanity', models.PositiveIntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, max_digits=3)),
                ('active_inventory', models.PositiveIntegerField(default=0)),
                ('total_sold', models.PositiveIntegerField(default=0)),
                ('Item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.Item')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_user.Store')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ItemSelectOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=3)),
                ('active_inventory', models.PositiveIntegerField(default=0)),
                ('total_sold', models.PositiveIntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SelectChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='numoption',
            name='item',
        ),
        migrations.RemoveField(
            model_name='numoption',
            name='store',
        ),
        migrations.RemoveField(
            model_name='selectoption',
            name='item',
        ),
        migrations.RemoveField(
            model_name='selectoption',
            name='selections',
        ),
        migrations.RemoveField(
            model_name='selectoption',
            name='store',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='items',
        ),
        migrations.DeleteModel(
            name='NumOption',
        ),
        migrations.DeleteModel(
            name='SelectOption',
        ),
        migrations.DeleteModel(
            name='SubOption',
        ),
        migrations.AddField(
            model_name='itemselectoption',
            name='choices',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.SelectChoice'),
        ),
        migrations.AddField(
            model_name='itemselectoption',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.Item'),
        ),
        migrations.AddField(
            model_name='itemselectoption',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_user.Store'),
        ),
        migrations.AddField(
            model_name='cartitemselectoption',
            name='selected',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='content.SelectChoice'),
        ),
        migrations.AddField(
            model_name='cartitemselectoption',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_user.Store'),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='noption',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.CartItemNumOption'),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='soption',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.CartItemSelectOption'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='cartItems',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='content.cartItem'),
            preserve_default=False,
        ),
    ]
