# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0013_question_rank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='desc_text',
            field=models.CharField(default=None, max_length=512, null=True, blank=True),
            preserve_default=True,
        ),
    ]
