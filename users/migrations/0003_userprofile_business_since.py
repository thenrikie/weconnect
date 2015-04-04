# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20150404_2152'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='business_since',
            field=models.DateTimeField(null=True, verbose_name='Business since'),
            preserve_default=True,
        ),
    ]
