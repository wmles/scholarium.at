# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 17:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Grundgeruest', '0002_auto_20171026_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ganzesmenue',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='hauptpunkt',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='unterpunkt',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, unique=True),
        ),
    ]