# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_auto_20150702_0746'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShowCase',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=1024)),
                ('user_profile', models.ForeignKey(to='users.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ShowCaseAttachment',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('caption', models.CharField(max_length=1024, blank=True)),
                ('file', models.FileField(upload_to=users.models.upload_filename, null=True, blank=True)),
                ('showcase', models.ForeignKey(to='users.ShowCase', related_name='attachment')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
