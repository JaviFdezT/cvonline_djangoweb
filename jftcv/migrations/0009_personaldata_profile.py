# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-09 01:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jftcv', '0008_digcomps'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaldata',
            name='profile',
            field=models.CharField(default='Information technology professional trained to participarte in technology projects with remarkable deadline sensitivity. Experience as a software developer with python, java and unix. Stron analytical, mathematical and statistical skills obtained through university period, including a stay abroad. Compatible team player through complete project cycles, testing and final implementation. Knowledge of foreign languages, driving licence, availability to travel in and outside the country.', max_length=300),
            preserve_default=False,
        ),
    ]
