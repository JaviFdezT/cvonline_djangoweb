# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-08 17:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jftcv', '0002_auto_20170308_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaldata',
            name='initials',
            field=models.CharField(default='jft', max_length=5),
            preserve_default=False,
        ),
    ]
