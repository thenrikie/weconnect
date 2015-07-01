# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0014_auto_20150629_0334'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='tag',
            field=models.CharField(default=None, max_length=512, null=True),
            preserve_default=True,
        ),
    ]
