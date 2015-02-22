# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
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
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
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
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(editable=False, max_length=25, choices=[('CUSTOMER', 'Customer'), ('COMPANY', 'Company')])),
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
                ('business', models.ManyToManyField(to='users.Business')),
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
