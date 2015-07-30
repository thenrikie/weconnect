# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='queue',
            name='finished_at',
            field=models.DateTimeField(default=None),
            preserve_default=True,
        ),
    ]
