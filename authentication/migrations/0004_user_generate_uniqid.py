# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from authentication.models import User

def generate_uniqid(apps, schema_editor):

    users = User.objects.filter(uniqid=None)
    for user in users:
        print(user.email)
        user.save()

class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_user_uniqid'),
    ]

    operations = [
        migrations.RunPython(
            generate_uniqid
        ),
    ]
