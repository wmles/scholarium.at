# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-04-26 20:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Grundgeruest', '0002_scholariumprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mitwirkende',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('text_de', models.TextField(blank=True, null=True)),
                ('text_en', models.TextField(blank=True, null=True)),
                ('link', models.CharField(blank=True, max_length=200, null=True)),
                ('level', models.CharField(max_length=30)),
                ('start', models.DateField(blank=True, null=True)),
                ('end', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Mitwirkender',
                'verbose_name_plural': 'Mitwirkende',
            },
        ),
    ]
