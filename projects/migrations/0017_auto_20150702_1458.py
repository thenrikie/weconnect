# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0016_auto_20150702_0345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='my_place',
            field=models.ForeignKey(related_name='my_place', to='users.District', verbose_name='I am located'),
            preserve_default=True,
        ),
    ]
