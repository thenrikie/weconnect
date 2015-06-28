# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_project_generate_uniqid'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='desc_text',
            field=models.CharField(default=None, null=True, max_length=512),
            preserve_default=True,
        ),
    ]
