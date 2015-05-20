# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pitches', '0002_auto_20150507_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pitch',
            name='price',
            field=models.FloatField(blank=True, verbose_name='Estimated Price', null=True),
            preserve_default=True,
        ),
    ]
