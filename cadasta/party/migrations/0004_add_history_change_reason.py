# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-09 06:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('party', '0003_convert_tenuretype_to_charfield'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalparty',
            name='history_change_reason',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='historicalpartyrelationship',
            name='history_change_reason',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='historicaltenurerelationship',
            name='history_change_reason',
            field=models.CharField(max_length=100, null=True),
        ),
    ]