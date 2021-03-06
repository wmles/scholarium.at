# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-05-09 22:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Veranstaltungen', '0005_auto_20170509_1521'),
    ]

    operations = [
        migrations.RenameField(
            model_name='veranstaltung',
            old_name='preis',
            new_name='preis_teilnahme',
        ),
        migrations.RemoveField(
            model_name='medium',
            name='arten_dicts',
        ),
        migrations.RemoveField(
            model_name='studiumdings',
            name='arten_dicts',
        ),
        migrations.RemoveField(
            model_name='veranstaltung',
            name='arten_dicts',
        ),
        migrations.AddField(
            model_name='medium',
            name='anzahl_aufzeichnung',
            field=models.SmallIntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='medium',
            name='anzahl_livestream',
            field=models.SmallIntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='medium',
            name='preis_aufzeichnung',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='medium',
            name='preis_livestream',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='studiumdings',
            name='anzahl_teilnahme',
            field=models.SmallIntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='studiumdings',
            name='preis_teilnahme',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='veranstaltung',
            name='anzahl_teilnahme',
            field=models.SmallIntegerField(blank=True, default=0),
        ),
    ]
