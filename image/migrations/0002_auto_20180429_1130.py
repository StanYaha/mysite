# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('image', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=32, blank=True)),
                ('caption', models.TextField(blank=True)),
                ('view_count', models.IntegerField(default=0)),
                ('like_count', models.IntegerField(default=0)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('shot_date', models.DateTimeField(null=True)),
                ('camera', models.CharField(max_length=128, blank=True)),
                ('square_loc', models.CharField(max_length=128, default='')),
                ('thumb_loc', models.CharField(max_length=128, default='')),
                ('middle_loc', models.CharField(max_length=128, default='')),
                ('original_loc', models.CharField(max_length=128, default='')),
                ('middle_width', models.IntegerField(default=0)),
                ('middle_height', models.IntegerField(default=0)),
                ('original_width', models.IntegerField(default=0)),
                ('original_height', models.IntegerField(default=0)),
                ('score', models.FloatField(default=0)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
