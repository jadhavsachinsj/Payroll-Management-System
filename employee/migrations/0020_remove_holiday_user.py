# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-12 11:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0019_auto_20180312_1633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='holiday',
            name='user',
        ),
    ]