# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-06 10:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0011_attendence'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Attendence',
            new_name='Attendance',
        ),
    ]
