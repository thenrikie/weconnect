# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0019_questionoption_other'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionoption',
            name='other',
            field=models.BooleanField(verbose_name='This is an other option', default=False),
            preserve_default=True,
        ),
    ]
