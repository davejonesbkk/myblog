# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-23 10:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'ordering': ['-created'], 'verbose_name': 'Blog Entry', 'verbose_name_plural': 'Blog Entries'},
        ),
    ]
