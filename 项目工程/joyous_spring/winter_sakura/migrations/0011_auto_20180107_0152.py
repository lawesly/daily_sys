# -*- coding: utf-8 -*-
# Generated by Django 1.11b1 on 2018-01-06 17:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('winter_sakura', '0010_auto_20180107_0147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='sex',
            field=models.CharField(choices=[('0', '男'), ('1', '女')], max_length=20, verbose_name='性别'),
        ),
    ]
