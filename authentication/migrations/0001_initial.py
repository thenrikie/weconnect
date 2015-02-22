# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('role', models.CharField(choices=[('CUSTOMER', 'Customer'), ('COMPANY', 'Company')], max_length=25, editable=False)),
                ('business_name', models.CharField(max_length=256)),
                ('mobile_number', models.CharField(max_length=100)),
                ('website', models.URLField(max_length=512)),
                ('desc', models.CharField(max_length=1024)),
                ('get_sms', models.BooleanField(default=False)),
                ('address_1', models.CharField(max_length=512)),
                ('address_2', models.CharField(max_length=512)),
                ('address_3', models.CharField(max_length=512)),
                ('address_4', models.CharField(max_length=512)),
                ('can_travel', models.BooleanField(default=False)),
                ('travel_distance', models.CharField(default=10, max_length=25, choices=[('10', '10 miles'), ('15', '15 miles'), ('20', '20 miles'), ('30', '30+ miles')])),
                ('only_remote', models.BooleanField(default=False)),
                ('customer_travel', models.BooleanField(default=False)),
                ('employees', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]