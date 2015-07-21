# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0018_auto_20150703_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionoption',
            name='other',
            field=models.BooleanField(default=False, verbose_name='Other option'),
            preserve_default=True,
        ),
    ]
