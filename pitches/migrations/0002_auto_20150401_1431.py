# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pitches', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pitch',
            name='project',
            field=models.ForeignKey(to='projects.Project'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='messageattachment',
            name='message',
            field=models.ForeignKey(related_name='attachment', to='pitches.Message'),
            preserve_default=True,
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
