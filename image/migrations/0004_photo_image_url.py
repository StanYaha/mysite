# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0003_remove_photo_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='image_url',
            field=models.CharField(max_length=128, default=''),
        ),
    ]
