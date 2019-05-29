# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-24 17:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0006_remove_post_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('C1', 'To Do'), ('C2', 'Doing'), ('C3', 'Done')], default='C1', max_length=50),
        ),
    ]