# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-09 17:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jftcv', '0010_auto_20170309_1616'),
    ]

    operations = [
        migrations.CreateModel(
            name='Router',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specifications', models.FileField(upload_to='router_specifications')),
            ],
        ),
    ]