# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pitches', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pitch',
            name='desc',
            field=models.CharField(null=True, verbose_name='Tell us why you would be the best person for this project', max_length=1024, blank=True),
            preserve_default=True,
        ),
    ]
