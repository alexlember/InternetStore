# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-24 04:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('UserId', models.AutoField(primary_key=True, serialize=False)),
                ('UserName', models.CharField(max_length=200)),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
    ]
