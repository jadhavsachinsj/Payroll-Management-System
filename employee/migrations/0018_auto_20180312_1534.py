# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-12 10:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0017_auto_20180307_1154'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.TextField(max_length=200)),
                ('website', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(blank=True, choices=[('D', 'Developer'), ('T', 'Tester'), ('H', 'HR'), ('M', 'Manager')], default='D', max_length=10)),
                ('prev_leave_allowed', models.IntegerField(default=0)),
                ('casual_leave_allowed', models.IntegerField(default=0)),
                ('salary', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('holiday_name', models.CharField(default='Sunday', max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='work_from_home',
        ),
        migrations.AddField(
            model_name='employee',
            name='alter_contact_no',
            field=models.CharField(default='0', max_length=12),
        ),
        migrations.AddField(
            model_name='employee',
            name='confirmation_period',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='employee',
            name='contact',
            field=models.CharField(default='0', max_length=12),
        ),
        migrations.AddField(
            model_name='salary',
            name='net_salary',
            field=models.IntegerField(default=0),
        ),
    ]