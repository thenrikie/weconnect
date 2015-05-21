# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_subbusiness_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subbusiness',
            name='desc',
            field=models.CharField(blank=True, max_length=255),
            preserve_default=True,
        ),
    ]
