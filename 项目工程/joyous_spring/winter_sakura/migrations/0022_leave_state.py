# -*- coding: utf-8 -*-
# Generated by Django 1.11b1 on 2018-01-13 07:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('winter_sakura', '0021_auto_20180111_0454'),
    ]

    operations = [
        migrations.AddField(
            model_name='leave',
            name='state',
            field=models.IntegerField(default=0, verbose_name='状态'),
        ),
    ]
