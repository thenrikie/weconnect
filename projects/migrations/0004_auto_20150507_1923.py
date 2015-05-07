# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20150507_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='travel_distance',
            field=models.ManyToManyField(to='users.District', related_name='project_travel_distance_set', blank=True),
            preserve_default=True,
        ),
    ]
