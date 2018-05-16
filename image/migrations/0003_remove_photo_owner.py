# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0002_auto_20180429_1130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='owner',
        ),
    ]
