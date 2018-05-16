# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('blog', '0002_auto_20180407_0910'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=taggit.managers.TaggableManager(verbose_name='Tags', help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag'),
        ),
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 11, 11, 25, 36, 250481, tzinfo=utc)),
        ),
    ]
