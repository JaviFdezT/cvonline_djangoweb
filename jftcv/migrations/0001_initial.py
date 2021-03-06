# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-08 14:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conferences',
            fields=[
                ('dates', models.CharField(max_length=60)),
                ('title', models.CharField(max_length=70)),
                ('organization', models.CharField(max_length=90)),
                ('description', models.CharField(max_length=120)),
                ('order', models.CharField(max_length=12, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('dates', models.CharField(max_length=60)),
                ('title', models.CharField(max_length=70)),
                ('organization', models.CharField(max_length=90)),
                ('description', models.CharField(max_length=120)),
                ('certificate', models.URLField()),
                ('order', models.CharField(max_length=12, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=20)),
                ('code', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=20)),
                ('phonenumber', models.CharField(max_length=20)),
                ('mail', models.CharField(max_length=30)),
                ('datebirth', models.CharField(max_length=20)),
                ('nationality', models.CharField(max_length=30)),
                ('linkedin', models.URLField()),
                ('github', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('dates', models.CharField(max_length=60)),
                ('position', models.CharField(max_length=70)),
                ('organization', models.CharField(max_length=90)),
                ('description', models.CharField(max_length=120)),
                ('certificate', models.URLField()),
                ('order', models.CharField(max_length=12, primary_key=True, serialize=False)),
            ],
        ),
    ]
