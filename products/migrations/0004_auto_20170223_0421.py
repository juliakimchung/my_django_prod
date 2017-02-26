# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 04:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.Customer'),
        ),
    ]
