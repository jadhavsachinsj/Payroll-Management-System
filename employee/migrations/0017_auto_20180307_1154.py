# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-07 06:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0016_attendance_mark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='leave_type',
            field=models.CharField(choices=[('n', 'enter'), ('s', 'SeekLeave'), ('c', 'CausualLeave')], default='n', max_length=3, null=True),
        ),
    ]
