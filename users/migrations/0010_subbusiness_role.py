# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20150520_1947'),
    ]

    operations = [
        migrations.AddField(
            model_name='subbusiness',
            name='role',
            field=models.CharField(max_length=255, blank=True),
            preserve_default=True,
        ),
    ]
