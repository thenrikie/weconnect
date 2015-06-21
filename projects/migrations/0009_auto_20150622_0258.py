# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20150520_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='urgency',
            field=models.CharField(choices=[('flexible', 'I can be flexible'), ('asap', 'As soon as possible'), ('week', 'Sometime this week'), ('specific', 'Specific date')], default='flexible', verbose_name='When do you need this service?', max_length=25),
            preserve_default=True,
        ),
    ]
