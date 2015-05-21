# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pitches', '0003_auto_20150520_1947'),
    ]

    operations = [
        migrations.AddField(
            model_name='pitch',
            name='accepted_at',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
    ]
