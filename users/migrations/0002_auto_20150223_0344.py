# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='facebook',
            field=models.CharField(default='', max_length=255),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='instagram',
            field=models.CharField(default='', max_length=255),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='linkedin',
            field=models.CharField(default='', max_length=255),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='pinterest',
            field=models.CharField(default='', max_length=255),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='twitter',
            field=models.CharField(default='', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='address_1',
            field=models.CharField(verbose_name='Room/Floor/Block', max_length=512),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='address_2',
            field=models.CharField(verbose_name='Street/Residential address', max_length=512),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='address_3',
            field=models.CharField(verbose_name='', max_length=512),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='address_4',
            field=models.CharField(verbose_name='Area', max_length=512),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='business_name',
            field=models.CharField(verbose_name='business name', max_length=256),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='can_travel',
            field=models.BooleanField(verbose_name='I can travel to my customers', default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='customer_travel',
            field=models.BooleanField(verbose_name='My customer usually travel to me', default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='desc',
            field=models.CharField(verbose_name='description', max_length=1024),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='employees',
            field=models.IntegerField(verbose_name='Employees number'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='get_sms',
            field=models.BooleanField(verbose_name='Send me an sms when I receive a job request', default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='mobile_number',
            field=models.CharField(verbose_name='mobile number', max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='only_remote',
            field=models.BooleanField(verbose_name='Only internet or phone', default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='travel_distance',
            field=models.CharField(verbose_name='How far will you travel', choices=[('10', '10 miles'), ('15', '15 miles'), ('20', '20 miles'), ('30', '30+ miles')], default=10, max_length=25),
            preserve_default=True,
        ),
    ]
