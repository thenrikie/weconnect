# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='service_desc',
            field=models.CharField(blank=True, max_length=1024, verbose_name='Your Services'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='desc',
            field=models.CharField(blank=True, max_length=1024, verbose_name='About Your Company'),
            preserve_default=True,
        ),
    ]
