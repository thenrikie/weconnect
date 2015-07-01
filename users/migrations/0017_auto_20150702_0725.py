# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_auto_20150702_0626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='address_area',
            field=models.ForeignKey(null=True, to='users.District', verbose_name='Area', related_name='area'),
            preserve_default=True,
        ),
    ]
