# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-10-18 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotes',
            name='author',
            field=models.CharField(default=1, max_length=225),
            preserve_default=False,
        ),
    ]
