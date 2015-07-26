# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_showcase_showcaseattachment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='showcaseattachment',
            name='showcase',
            field=models.ForeignKey(related_name='attachments', to='users.ShowCase'),
            preserve_default=True,
        ),
    ]
