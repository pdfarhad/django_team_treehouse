# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-28 00:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0012_course_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='status',
        ),
    ]
