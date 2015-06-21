# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20150608_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='mobile_number',
            field=models.CharField(verbose_name='mobile number', max_length=100),
            preserve_default=True,
        ),
    ]
