# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2023-02-10 12:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='mobno',
            field=models.CharField(max_length=10),
        ),
    ]
