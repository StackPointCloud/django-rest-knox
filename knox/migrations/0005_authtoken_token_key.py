# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-18 09:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knox', '0004_authtoken_expires'),
    ]

    operations = [
        migrations.AddField(
            model_name='authtoken',
            name='token_key',
            field=models.CharField(db_index=True, default='', max_length=8),
            preserve_default=False,
        ),
    ]
