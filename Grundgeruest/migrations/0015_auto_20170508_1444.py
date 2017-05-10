# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-05-08 12:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Grundgeruest', '0014_auto_20170505_1708'),
    ]

    operations = [
        migrations.CreateModel(
            name='NurAktive',
            fields=[
                ('mitwirkende_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Grundgeruest.Mitwirkende')),
            ],
            bases=('Grundgeruest.mitwirkende',),
        ),
        migrations.AlterModelOptions(
            name='mitwirkende',
            options={'ordering': ('level', 'start', 'id_old'), 'verbose_name': 'Mitwirkender', 'verbose_name_plural': 'Mitwirkende'},
        ),
    ]