# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-01 16:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0012_articles_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
