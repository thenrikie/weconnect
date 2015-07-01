# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20150702_0606'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='address_area',
            field=models.ForeignKey(default=30, to='users.District', verbose_name='Area', related_name='area'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='address_4',
            field=models.CharField(blank=True, verbose_name='', max_length=512),
            preserve_default=True,
        ),
    ]
