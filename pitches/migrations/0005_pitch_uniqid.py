# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pitches', '0004_pitch_accepted_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='pitch',
            name='uniqid',
            field=models.CharField(max_length=16, editable=False, unique=True, null=True),
            preserve_default=True,
        ),
    ]
