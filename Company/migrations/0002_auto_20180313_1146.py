# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-13 06:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='fax',
            field=models.TextField(blank=True, max_length=50, null=True),
        ),
    ]
