# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-05-04 13:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('Produkte', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kauf',
            name='produkt',
        ),
        migrations.RemoveField(
            model_name='produkt',
            name='kaeufe',
        ),
        migrations.AddField(
            model_name='kauf',
            name='produkt_model',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contenttypes.ContentType'),
        ),
    ]
