# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_userprofile_google'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='work_attach_1',
            field=models.FileField(null=True, upload_to=users.models.workattach_filename, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='work_attach_2',
            field=models.FileField(null=True, upload_to=users.models.workattach_filename, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='work_attach_3',
            field=models.FileField(null=True, upload_to=users.models.workattach_filename, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='work_image_1',
            field=models.ImageField(null=True, upload_to=users.models.workimage_filename, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='work_image_2',
            field=models.ImageField(null=True, upload_to=users.models.workimage_filename, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='work_image_3',
            field=models.ImageField(null=True, upload_to=users.models.workimage_filename, blank=True),
            preserve_default=True,
        ),
    ]
