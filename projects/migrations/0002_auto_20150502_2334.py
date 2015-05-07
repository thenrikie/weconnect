# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='cancelled',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='cancelled_reason',
            field=models.CharField(null=True, max_length=25, choices=[('no_help_needed', 'I no longer need help with this project'), ('found_someone', 'I have found someone else to help me'), ('no_right_candidate', 'The companies I was introduced to are not right for this project'), ('other', 'Other')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='cancelled_reason_other',
            field=models.CharField(null=True, max_length=1024),
            preserve_default=True,
        ),
    ]
