# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_userprofile_business_since'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='google',
            field=models.CharField(max_length=255, default='', blank=True),
            preserve_default=True,
        ),
    ]
