# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20150522_0241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='website',
            field=models.CharField(max_length=512, validators=[django.core.validators.URLValidator(schemes=['https', 'http'])], blank=True),
            preserve_default=True,
        ),
    ]
