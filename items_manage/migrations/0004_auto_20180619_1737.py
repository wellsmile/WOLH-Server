# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-19 09:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items_manage', '0003_auto_20180619_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Item ID'),
        ),
        migrations.AlterField(
            model_name='items',
            name='name',
            field=models.CharField(db_index=True, max_length=256, unique=True, verbose_name='Item Name'),
        ),
        migrations.AlterField(
            model_name='operation',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Operation ID'),
        ),
    ]
