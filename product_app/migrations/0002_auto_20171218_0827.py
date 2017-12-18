# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-18 08:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockoperation',
            name='location',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, related_name='location', to='product_app.Location'),
        ),
        migrations.AlterField(
            model_name='stockoperation',
            name='product',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, related_name='product', to='product_app.Product'),
        ),
    ]
