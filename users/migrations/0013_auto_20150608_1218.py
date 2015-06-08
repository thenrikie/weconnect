# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20150528_2012'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='rank',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='business',
            name='desc',
            field=models.CharField(blank=True, max_length=255),
            preserve_default=True,
        ),
    ]
