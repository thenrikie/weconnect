# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20150516_1839'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='uniqid',
            field=models.CharField(max_length=16, null=True, editable=False, unique=True),
            preserve_default=True,
        ),
    ]
