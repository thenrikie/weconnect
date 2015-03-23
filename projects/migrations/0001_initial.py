# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('urgency', models.CharField(max_length=25, verbose_name='When do you need this service?', default='flexible', choices=[('flexible', 'I can be flexible'), ('asap', 'As soon as possible'), ('week', 'Sometime this week'), ('specific', 'Specific date'), ('other', 'Other')])),
                ('deadline', models.DateTimeField(null=True)),
                ('budget_lower', models.FloatField(blank=True, null=True)),
                ('budget_upper', models.FloatField(blank=True, null=True)),
                ('can_travel', models.BooleanField(verbose_name='I can travel to them', default=False)),
                ('company_travel', models.BooleanField(verbose_name='They travel to me', default=False)),
                ('travel_distance', models.CharField(max_length=25, verbose_name='How far will you travel', default='Central & Western', choices=[('Islands', 'Islands'), ('Kwai Tsing', 'Kwai Tsing'), ('North', 'North'), ('Sha Tin', 'Sha Tin'), ('Tai Po', 'Tai Po'), ('Tsuen Wan', 'Tsuen Wan'), ('Tuen Mun', 'Tuen Mun'), ('Yuen Long', 'Yuen Long'), ('Kowloon City', 'Kowloon City'), ('Kwun Tong', 'Kwun Tong'), ('Sham Shui Po', 'Sham Shui Po'), ('Wong Tai Sin', 'Wong Tai Sin'), ('Yau Tsim Mong', 'Yau Tsim Mong'), ('Central & Western', 'Central & Western'), ('Eastern', 'Eastern'), ('Southern', 'Southern'), ('Wan Chai', 'Wan Chai')])),
                ('my_place', models.CharField(max_length=25, verbose_name='', default='Central & Western', choices=[('Islands', 'Islands'), ('Kwai Tsing', 'Kwai Tsing'), ('North', 'North'), ('Sha Tin', 'Sha Tin'), ('Tai Po', 'Tai Po'), ('Tsuen Wan', 'Tsuen Wan'), ('Tuen Mun', 'Tuen Mun'), ('Yuen Long', 'Yuen Long'), ('Kowloon City', 'Kowloon City'), ('Kwun Tong', 'Kwun Tong'), ('Sham Shui Po', 'Sham Shui Po'), ('Wong Tai Sin', 'Wong Tai Sin'), ('Yau Tsim Mong', 'Yau Tsim Mong'), ('Central & Western', 'Central & Western'), ('Eastern', 'Eastern'), ('Southern', 'Southern'), ('Wan Chai', 'Wan Chai')])),
                ('desc', models.CharField(blank=True, max_length=1024, verbose_name='description')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('business', models.ManyToManyField(to='users.Business')),
                ('sub_business', models.ManyToManyField(to='users.SubBusiness')),
                ('user', models.ForeignKey(to='authentication.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
