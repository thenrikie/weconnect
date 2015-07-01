# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20150622_0258'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='district',
            options={'ordering': ['rank']},
        ),
        migrations.AddField(
            model_name='district',
            name='rank',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
    ]
