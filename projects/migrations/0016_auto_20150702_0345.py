# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0015_question_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='rank',
            field=models.IntegerField(null=True, blank=True, default=None),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='tag',
            field=models.CharField(null=True, blank=True, default=None, max_length=512),
            preserve_default=True,
        ),
    ]
