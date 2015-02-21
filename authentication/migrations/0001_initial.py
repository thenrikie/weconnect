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
            name='UserProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('role', models.CharField(max_length=25)),
                ('business_name', models.CharField(max_length=256)),
                ('mobile_number', models.CharField(max_length=100)),
                ('website', models.URLField(max_length=512)),
                ('desc', models.CharField(max_length=1024)),
                ('get_sms', models.BooleanField()),
                ('address_1', models.CharField(max_length=512)),
                ('address_2', models.CharField(max_length=512)),
                ('address_3', models.CharField(max_length=512)),
                ('address_4', models.CharField(max_length=512)),
                ('can_travel', models.BooleanField()),
                ('travel_distance', models.CharField(choices=[('10', '10 miles'), ('15', '15 miles'), ('20', '20 miles'), ('30', '30+ miles')], max_length=25, default=10)),
                ('only_remote', models.BooleanField()),
                ('customer_travel', models.BooleanField()),
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
