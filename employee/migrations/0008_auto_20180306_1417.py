# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-06 08:47
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0007_salary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salary',
            name='HRA',
        ),
        migrations.AddField(
            model_name='salary',
            name='conv_allowence',
            field=models.FloatField(default='0.0'),
        ),
        migrations.AddField(
            model_name='salary',
            name='hra',
            field=models.FloatField(default='0.0'),
        ),
        migrations.AddField(
            model_name='salary',
            name='prof_tax',
            field=models.DecimalField(decimal_places=4, default=Decimal('0.0000'), max_digits=20),
        ),
        migrations.AddField(
            model_name='salary',
            name='special_allowence',
            field=models.FloatField(default='0.0'),
        ),
    ]
