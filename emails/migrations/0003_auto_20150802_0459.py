# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0002_queue_finished_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queue',
            name='finished_at',
            field=models.DateTimeField(default=None, null=True),
            preserve_default=True,
        ),
    ]
