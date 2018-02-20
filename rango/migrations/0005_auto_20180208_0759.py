# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0004_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('content', models.TextField()),
                ('category', models.ForeignKey(to='rango.Category')),
            ],
            options={
                'ordering': ('-pub_date',),
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='page',
            name='views',
            field=models.IntegerField(default=12),
            preserve_default=True,
        ),
    ]
