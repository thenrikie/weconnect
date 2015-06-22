# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from pitches.models import Pitch

def generate_uniqid(apps, schema_editor):

    pitches = Pitch.objects.filter(uniqid=None)
    for pitch in pitches:
        pitch.save()

class Migration(migrations.Migration):

    dependencies = [
        ('pitches', '0005_pitch_uniqid'),
    ]

    operations = [
        migrations.RunPython(
            generate_uniqid
        ),
    ]
