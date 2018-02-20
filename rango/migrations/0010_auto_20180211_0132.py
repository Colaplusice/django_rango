# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0009_auto_20180211_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(unique=True, max_length=128),
            preserve_default=True,
        ),
    ]
