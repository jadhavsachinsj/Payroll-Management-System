# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-29 04:36
from __future__ import unicode_literals

from decimal import Decimal
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DepartmentHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Department')),
            ],
        ),
        migrations.CreateModel(
            name='DesignationHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('designation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Designation')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(default='0', max_length=12)),
                ('birth_date', models.DateField()),
                ('salary', models.DecimalField(decimal_places=4, default=Decimal('0.0000'), max_digits=10)),
                ('address', models.TextField(max_length=200)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('profile_photo', models.ImageField(null=True, upload_to='payroll')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Company')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JobTypeHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Employee')),
                ('jobtype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.JobType')),
            ],
        ),
        migrations.CreateModel(
            name='LeaveHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('peivilege_leave', models.CharField(blank=True, max_length=50)),
                ('casual_leave', models.CharField(blank=True, max_length=50)),
                ('attendance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.LeaveHistory')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Employee')),
            ],
        ),
        migrations.AddField(
            model_name='designationhistory',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Employee'),
        ),
        migrations.AddField(
            model_name='departmenthistory',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Employee'),
        ),
    ]
