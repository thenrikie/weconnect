# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import pitches.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
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
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('file', models.FileField(null=True, blank=True, upload_to=pitches.models.upload_filename)),
                ('message', models.ForeignKey(related_name='attachment', to='pitches.Message')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pitch',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('archived', models.BooleanField(default=False)),
                ('price', models.FloatField(null=True, blank=True)),
                ('desc', models.CharField(verbose_name='description', blank=True, null=True, max_length=1024)),
                ('rate', models.CharField(default='total', choices=[('hourly', 'Hourly Rate'), ('total', 'Estimated project cost'), ('NA', 'I do not want to provide a price yet')], null=True, max_length=25)),
                ('state', models.CharField(default='waiting', choices=[('waiting', 'Waiting'), ('accepted', 'Company Accepted'), ('hired', 'Hired'), ('rejected', 'Customer rejected'), ('company_rejected', 'Company rejected')], max_length=25)),
                ('state_changed_at', models.DateTimeField()),
                ('hired_at', models.DateTimeField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(to='projects.Project')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='message',
            name='pitch',
            field=models.ForeignKey(to='pitches.Pitch'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='message',
            name='recipient',
            field=models.ForeignKey(related_name='recipient', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(related_name='sender', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
