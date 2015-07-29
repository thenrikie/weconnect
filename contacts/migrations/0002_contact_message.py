# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='message',
            field=models.CharField(max_length=1024, verbose_name='message', blank=True),
            preserve_default=True,
        ),
    ]
