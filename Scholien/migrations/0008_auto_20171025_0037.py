# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 00:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Scholien', '0007_auto_20170531_1731'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artikel',
            options={'ordering': ['-datum_publizieren'], 'verbose_name': 'Artikel', 'verbose_name_plural': 'Artikel'},
        ),
        migrations.AlterModelOptions(
            name='buechlein',
            options={'ordering': ['-alte_nr'], 'verbose_name': 'Büchlein', 'verbose_name_plural': 'Büchlein'},
        ),
    ]