# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20150516_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='my_place',
            field=models.ForeignKey(related_name='my_place', verbose_name='The pro travel to me', to='users.District'),
            preserve_default=True,
        ),
    ]
