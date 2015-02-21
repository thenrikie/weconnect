# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20150221_0355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='role',
            field=models.CharField(editable=False, choices=[('CUSTOMER', 'Customer'), ('COMPANY', 'Company')], max_length=25),
            preserve_default=True,
        ),
    ]
