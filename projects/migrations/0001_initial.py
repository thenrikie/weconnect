# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('urgency', models.CharField(default='flexible', choices=[('flexible', 'I can be flexible'), ('asap', 'As soon as possible'), ('week', 'Sometime this week'), ('specific', 'Specific date'), ('other', 'Other')], verbose_name='When do you need this service?', max_length=25)),
                ('deadline', models.DateTimeField(null=True)),
                ('budget_lower', models.FloatField(null=True, blank=True)),
                ('budget_upper', models.FloatField(null=True, blank=True)),
                ('can_travel', models.BooleanField(default=False, verbose_name='I can travel to them')),
                ('company_travel', models.BooleanField(default=False, verbose_name='They travel to me')),
                ('desc', models.CharField(verbose_name='Anything else they should know', blank=True, max_length=1024)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('business', models.ManyToManyField(to='users.Business')),
                ('my_place', models.ForeignKey(related_name='my_place', to='users.District')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('type', models.CharField(choices=[('CheckboxSelectMultiple', 'CheckboxSelectMultiple'), ('Select', 'Select'), ('RadioSelect', 'RadioSelect')], verbose_name='', max_length=25)),
                ('text', models.CharField(max_length=512)),
                ('sub_business', models.ForeignKey(to='users.SubBusiness')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='QuestionOption',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('text', models.CharField(max_length=512)),
                ('question', models.ForeignKey(to='projects.Question')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='project',
            name='question_option',
            field=models.ManyToManyField(to='projects.QuestionOption'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='sub_business',
            field=models.ManyToManyField(to='users.SubBusiness'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='travel_distance',
            field=models.ManyToManyField(to='users.District', related_name='project_travel_distance_set'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
