# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knox', '0003_auto_20150916_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='authtoken',
            name='expires',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='authtoken',
            name='name',
            field=models.CharField(default=b'', max_length=200),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='authtoken',
            name='is_system',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
