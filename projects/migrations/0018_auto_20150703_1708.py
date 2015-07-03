# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0017_auto_20150702_1458'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionAnswer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('text', models.CharField(max_length=512)),
                ('project', models.ForeignKey(to='projects.Project')),
                ('question', models.ForeignKey(to='projects.Question')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='question',
            name='type',
            field=models.CharField(verbose_name='', choices=[('CheckboxSelectMultiple', 'CheckboxSelectMultiple'), ('Select', 'Select'), ('RadioSelect', 'RadioSelect'), ('Text', 'Text')], max_length=25),
            preserve_default=True,
        ),
    ]
