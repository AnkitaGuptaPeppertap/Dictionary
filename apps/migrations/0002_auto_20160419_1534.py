# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-19 15:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BookmarkWords',
            new_name='BookmarkWord',
        ),
    ]
