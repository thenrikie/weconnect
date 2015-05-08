# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20150507_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='business_since',
            field=models.CharField(max_length=255, verbose_name='Business since', null=True),
            preserve_default=True,
        ),
    ]
