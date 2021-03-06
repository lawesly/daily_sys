# -*- coding: utf-8 -*-
# Generated by Django 1.11b1 on 2018-01-14 07:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('winter_sakura', '0026_remove_leave_staff_dept'),
    ]

    operations = [
        migrations.AddField(
            model_name='daily',
            name='late_and_leave_staff',
            field=models.IntegerField(default=0, verbose_name='迟到并且早退员工数'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='daily',
            name='check_staff',
            field=models.IntegerField(verbose_name='正常考勤员工数'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='sex',
            field=models.CharField(choices=[('1', '女'), ('0', '男')], max_length=20, verbose_name='性别'),
        ),
    ]
