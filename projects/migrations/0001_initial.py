# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20150305_0253'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('urgency', models.CharField(choices=[('flexible', 'I can be flexible'), ('asap', 'As soon as possible'), ('week', 'Sometime this week'), ('specific', 'Specific date'), ('other', 'Other')], default='flexible', max_length=25, verbose_name='When do you need this service?')),
                ('deadline', models.DateTimeField()),
                ('budget_lower', models.FloatField(blank=True)),
                ('budget_upper', models.FloatField(blank=True)),
                ('can_travel', models.BooleanField(default=False, verbose_name='I can travel to them')),
                ('company_travel', models.BooleanField(default=False, verbose_name='They travel to me')),
                ('travel_distance', models.CharField(choices=[('10', '10 miles'), ('15', '15 miles'), ('20', '20 miles'), ('30', '30+ miles')], default=10, max_length=25, verbose_name='How far will you travel')),
                ('desc', models.CharField(blank=True, max_length=1024, verbose_name='description')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('business', models.ManyToManyField(to='users.Business')),
                ('sub_business', models.ManyToManyField(to='users.SubBusiness')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
