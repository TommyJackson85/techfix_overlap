# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-14 19:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0003_auto_20190510_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]
