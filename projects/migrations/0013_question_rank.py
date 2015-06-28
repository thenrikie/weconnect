# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_question_desc_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='rank',
            field=models.IntegerField(null=True, default=None),
            preserve_default=True,
        ),
    ]
