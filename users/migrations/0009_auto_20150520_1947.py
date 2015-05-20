# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_userprofile_travel_to_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='travel_to_customer',
            field=models.CharField(default='anywhere', verbose_name='I can travel to my customers', max_length=25, choices=[('anywhere', 'Anywhere in Hong Kong'), ('some_areas', 'Only some areas in Hong Kong')]),
            preserve_default=True,
        ),
    ]
