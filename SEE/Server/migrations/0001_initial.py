# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-15 09:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.CharField(choices=[('m', 'male'), ('f', 'female')], max_length=2, verbose_name='sex')),
                ('age', models.IntegerField(blank=True, default=0, verbose_name='age')),
                ('dept', models.CharField(blank=True, max_length=50, verbose_name='department')),
                ('post', models.CharField(blank=True, max_length=50, verbose_name='post')),
                ('title', models.CharField(blank=True, max_length=50, verbose_name='title')),
                ('phone', models.IntegerField(blank=True, verbose_name='phone')),
                ('address', models.CharField(max_length=50, verbose_name='address')),
                ('hospital', models.CharField(max_length=50, verbose_name='hospital')),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'doctor',
                'verbose_name_plural': 'doctor',
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthday', models.DateTimeField(blank=True, null=True, verbose_name='birth day')),
                ('add', models.CharField(blank=True, max_length=50, verbose_name='address')),
                ('health', models.CharField(blank=True, max_length=200, verbose_name='health')),
                ('ps', models.CharField(blank=True, max_length=200, verbose_name='ps')),
                ('idnum', models.IntegerField(verbose_name='idcard')),
                ('occupation', models.CharField(max_length=50, verbose_name='occupation')),
                ('diagnose', models.TextField(default='nothing', verbose_name='diagnose')),
                ('sex', models.CharField(choices=[('m', 'male'), ('f', 'female')], max_length=2, verbose_name='sex')),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'patient',
                'verbose_name_plural': 'patient',
            },
        ),
    ]