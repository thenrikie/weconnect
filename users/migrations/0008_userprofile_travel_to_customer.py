# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20150508_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='travel_to_customer',
            field=models.CharField(max_length=25, default='anywhere', verbose_name='I can travel to my customers', choices=[('anywhere', 'Anywhere in Hong Kong'), ('some_areas', 'Only some areas in Hong Kong'), ('no', 'I need the pro only to travel to me')]),
            preserve_default=True,
        ),
    ]
