# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20150223_0344'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='logo',
            field=models.ImageField(null=True, upload_to='photos/orgs/'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(null=True, upload_to='photos/persons/'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='address_1',
            field=models.CharField(verbose_name='Room/Floor/Block', max_length=512, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='address_2',
            field=models.CharField(verbose_name='Street/Residential address', max_length=512, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='address_3',
            field=models.CharField(verbose_name='', max_length=512, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='address_4',
            field=models.CharField(verbose_name='Area', max_length=512, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='desc',
            field=models.CharField(verbose_name='description', max_length=1024, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='employees',
            field=models.IntegerField(default=0, verbose_name='Employees number'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='facebook',
            field=models.CharField(default='', max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='instagram',
            field=models.CharField(default='', max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='linkedin',
            field=models.CharField(default='', max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='mobile_number',
            field=models.CharField(verbose_name='mobile number', max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='pinterest',
            field=models.CharField(default='', max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='twitter',
            field=models.CharField(default='', max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='website',
            field=models.URLField(max_length=512, blank=True),
            preserve_default=True,
        ),
    ]
