# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-06 23:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelo', '0002_auto_20181031_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='direccion',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='telefono',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
