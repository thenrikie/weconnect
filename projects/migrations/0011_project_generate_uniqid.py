# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from projects.models import Project

def generate_uniqid(apps, schema_editor):

    projects = Project.objects.filter(uniqid=None)
    for project in projects:
        project.save()

class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_project_uniqid'),
    ]

    operations = [
        migrations.RunPython(
            generate_uniqid
        ),
    ]
