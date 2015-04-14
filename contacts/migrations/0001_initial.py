# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email address')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='business name')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
