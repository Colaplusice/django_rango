# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2018-01-29 08:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20180129_0810'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=2, unique=True),
            preserve_default=False,
        ),
    ]
