# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-05 10:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_auto_20180305_1524'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='leave_left',
        ),
    ]