# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_auto_20150516_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='specific_date',
            field=models.DateField(blank=True, verbose_name='Date', null=True),
            preserve_default=True,
        ),
    ]
