# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-01 12:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='timestamp',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2016, 4, 1, 12, 59, 24, 608505, tzinfo=utc)),
        ),
    ]
