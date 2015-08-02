# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0003_auto_20150802_0459'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='queue',
            options={'ordering': ['-created_at']},
        ),
    ]
