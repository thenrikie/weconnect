# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_auto_20150702_0725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='employees',
            field=models.IntegerField(default=1, verbose_name='Employees number'),
            preserve_default=True,
        ),
    ]
