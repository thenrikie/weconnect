# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20150507_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='specific_date',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
    ]
