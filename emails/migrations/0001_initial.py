# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Queue',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('item_id', models.IntegerField()),
                ('item_object', models.CharField(max_length=255)),
                ('action', models.CharField(max_length=255)),
                ('start_at', models.DateTimeField()),
                ('before_at', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('state', models.CharField(choices=[('waiting', 'waiting'), ('processing', 'processing'), ('finished', 'finished')], max_length=255, default='waiting')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
