# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import pitches.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=4096)),
                ('read', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MessageAttachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=pitches.models.upload_filename, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pitch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archived', models.BooleanField(default=False)),
                ('price', models.FloatField(null=True, blank=True)),
                ('desc', models.CharField(null=True, verbose_name='description', blank=True, max_length=1024)),
                ('rate', models.CharField(choices=[('hourly', 'Hourly Rate'), ('total', 'Estimated project cost'), ('NA', 'I do not want to provide a price yet')], null=True, default='total', max_length=25)),
                ('state', models.CharField(choices=[('waiting', 'Waiting'), ('accepted', 'Company Accepted'), ('hired', 'Hired'), ('rejected', 'Customer rejected'), ('company_rejected', 'Company rejected')], default='waiting', max_length=25)),
                ('state_changed_at', models.DateTimeField()),
                ('hired_at', models.DateTimeField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
