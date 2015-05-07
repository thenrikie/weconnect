# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20150502_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='cancelled_reason',
            field=models.CharField(default=None, null=True, max_length=25, choices=[('no_help_needed', 'I no longer need help with this project'), ('found_someone', 'I have found someone else to help me'), ('no_right_candidate', 'The companies I was introduced to are not right for this project'), ('other', 'Other')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='cancelled_reason_other',
            field=models.CharField(max_length=1024, null=True, blank=True),
            preserve_default=True,
        ),
    ]
