# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-05-05 15:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Grundgeruest', '0013_mitwirkende_id_old'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mitwirkende',
            options={'ordering': '', 'verbose_name': 'Mitwirkender', 'verbose_name_plural': 'Mitwirkende'},
        ),
        migrations.AlterField(
            model_name='mitwirkende',
            name='id_old',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='mitwirkende',
            name='level',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]