# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('desc', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SubBusiness',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
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
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('role', models.CharField(editable=False, max_length=25, choices=[('CUSTOMER', 'Customer'), ('COMPANY', 'Company')])),
                ('business_name', models.CharField(max_length=256, verbose_name='business name')),
                ('mobile_number', models.CharField(blank=True, max_length=100, verbose_name='mobile number')),
                ('website', models.URLField(blank=True, max_length=512)),
                ('desc', models.CharField(blank=True, max_length=1024, verbose_name='description')),
                ('get_sms', models.BooleanField(verbose_name='Send me an sms when I receive a job request', default=False)),
                ('address_1', models.CharField(blank=True, max_length=512, verbose_name='Room/Floor/Block')),
                ('address_2', models.CharField(blank=True, max_length=512, verbose_name='Street/Residential address')),
                ('address_3', models.CharField(blank=True, max_length=512, verbose_name='')),
                ('address_4', models.CharField(blank=True, max_length=512, verbose_name='Area')),
                ('can_travel', models.BooleanField(verbose_name='I can travel to my customers', default=False)),
                ('travel_distance', models.CharField(max_length=25, verbose_name='How far will you travel', default=10, choices=[('10', '10 miles'), ('15', '15 miles'), ('20', '20 miles'), ('30', '30+ miles')])),
                ('only_remote', models.BooleanField(verbose_name='Only internet or phone', default=False)),
                ('customer_travel', models.BooleanField(verbose_name='My customer usually travel to me', default=False)),
                ('employees', models.IntegerField(verbose_name='Employees number', default=0)),
                ('facebook', models.CharField(blank=True, max_length=255, default='')),
                ('linkedin', models.CharField(blank=True, max_length=255, default='')),
                ('twitter', models.CharField(blank=True, max_length=255, default='')),
                ('pinterest', models.CharField(blank=True, max_length=255, default='')),
                ('instagram', models.CharField(blank=True, max_length=255, default='')),
                ('photo', models.ImageField(blank=True, null=True, upload_to=users.models.person_filename)),
                ('logo', models.ImageField(blank=True, null=True, upload_to=users.models.logo_filename)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('business', models.ManyToManyField(to='users.Business')),
                ('user', models.OneToOneField(to='authentication.User')),
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
