# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-05-04 13:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Produkte', '0002_auto_20170504_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='kauf',
            name='produkt_art',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='kauf',
            name='produkt_id',
            field=models.SmallIntegerField(null=True),
        ),
    ]
