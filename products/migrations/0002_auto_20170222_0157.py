# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 01:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Order',
            new_name='Orders',
        ),
    ]
