# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20150507_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='travel_distance',
            field=models.ManyToManyField(related_name='userprofile_travel_distance_set', verbose_name='How far will you travel', blank=True, to='users.District'),
            preserve_default=True,
        ),
    ]
