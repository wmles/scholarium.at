# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-10-02 10:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bibliothek', '0005_auto_20171001_1105'),
    ]

    operations = [
        migrations.AddField(
            model_name='buch',
            name='alte_nr',
            field=models.SmallIntegerField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='buch',
            name='bild',
            field=models.ImageField(blank=True, null=True, upload_to='scholienbuechlein'),
        ),
        migrations.AddField(
            model_name='buch',
            name='epub',
            field=models.FileField(blank=True, null=True, upload_to='scholienbuechlein'),
        ),
        migrations.AddField(
            model_name='buch',
            name='mobi',
            field=models.FileField(blank=True, null=True, upload_to='scholienbuechlein'),
        ),
        migrations.AddField(
            model_name='buch',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='scholienbuechlein'),
        ),
    ]
