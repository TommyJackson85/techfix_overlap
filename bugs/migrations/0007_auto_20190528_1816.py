# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-28 18:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0006_remove_post_tag'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment',
            new_name='BugComment',
        ),
        migrations.RenameModel(
            old_name='Post',
            new_name='BugPost',
        ),
    ]
