# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-05-10 14:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Scholien', '0004_buechlein_alte_nr'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='buechlein',
            options={'ordering': ['-alte_nr'], 'verbose_name_plural': 'Büchlein'},
        ),
    ]
