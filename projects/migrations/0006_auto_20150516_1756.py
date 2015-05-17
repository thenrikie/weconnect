# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_project_specific_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='travel_to_pro',
            field=models.CharField(default='anywhere', max_length=25, verbose_name='I can travel to the pro', choices=[('anywhere', 'Anywhere in Hong Kong'), ('some_areas', 'Only some areas in Hong Kong'), ('no', 'I need the pro only to travel to me')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='can_travel',
            field=models.BooleanField(default=False, verbose_name='I can travel to the pro'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='specific_date',
            field=models.DateTimeField(null=True, verbose_name='Date', blank=True),
            preserve_default=True,
        ),
    ]
