# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_auto_20150622_0258'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='uniqid',
            field=models.CharField(max_length=16, editable=False, unique=True, null=True),
            preserve_default=True,
        ),
    ]
