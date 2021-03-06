# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('artist', models.CharField(max_length=30)),
                ('album_title', models.CharField(max_length=40)),
                ('genre', models.CharField(max_length=50)),
                ('album_logo', models.CharField(max_length=260)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file_type', models.CharField(max_length=40)),
                ('song_title', models.CharField(max_length=250)),
                ('album', models.ForeignKey(to='shashank.Album')),
            ],
        ),
    ]
