# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import users.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('desc', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('text', models.CharField(max_length=512)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SubBusiness',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('desc', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('role', models.CharField(choices=[('CUSTOMER', 'Customer'), ('COMPANY', 'Company')], editable=False, max_length=25)),
                ('business_name', models.CharField(verbose_name='business name', max_length=256)),
                ('mobile_number', models.CharField(verbose_name='mobile number', blank=True, max_length=100)),
                ('website', models.URLField(blank=True, max_length=512)),
                ('desc', models.CharField(verbose_name='description', blank=True, max_length=1024)),
                ('get_sms', models.BooleanField(default=False, verbose_name='Send me an sms when I receive a job request')),
                ('address_1', models.CharField(verbose_name='Room/Floor/Block', blank=True, max_length=512)),
                ('address_2', models.CharField(verbose_name='Street/Residential address', blank=True, max_length=512)),
                ('address_3', models.CharField(verbose_name='', blank=True, max_length=512)),
                ('address_4', models.CharField(verbose_name='Area', blank=True, max_length=512)),
                ('can_travel', models.BooleanField(default=False, verbose_name='I can travel to my customers')),
                ('only_remote', models.BooleanField(default=False, verbose_name='Only internet or phone')),
                ('customer_travel', models.BooleanField(default=False, verbose_name='My customer usually travel to me')),
                ('employees', models.IntegerField(default=0, verbose_name='Employees number')),
                ('facebook', models.CharField(default='', blank=True, max_length=255)),
                ('linkedin', models.CharField(default='', blank=True, max_length=255)),
                ('twitter', models.CharField(default='', blank=True, max_length=255)),
                ('pinterest', models.CharField(default='', blank=True, max_length=255)),
                ('instagram', models.CharField(default='', blank=True, max_length=255)),
                ('photo', models.ImageField(null=True, blank=True, upload_to=users.models.person_filename)),
                ('logo', models.ImageField(null=True, blank=True, upload_to=users.models.logo_filename)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('business', models.ManyToManyField(to='users.Business')),
                ('sub_business', models.ManyToManyField(to='users.SubBusiness')),
                ('travel_distance', models.ManyToManyField(to='users.District', related_name='userprofile_travel_distance_set', verbose_name='How far will you travel')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='business',
            name='sub_business',
            field=models.ManyToManyField(to='users.SubBusiness'),
            preserve_default=True,
        ),
    ]
