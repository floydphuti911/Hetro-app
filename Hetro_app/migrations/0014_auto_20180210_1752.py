# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-10 17:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hetro_app', '0013_album_trending'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='art',
            field=models.ImageField(blank=True, default='default-album.png', null=True, upload_to='album_art'),
        ),
    ]
