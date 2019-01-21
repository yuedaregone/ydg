# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-21 01:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skv',
            fields=[
                ('id', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('key', models.TextField(blank=True, null=True)),
                ('value', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Skv',
                'managed': False,
            },
        ),
    ]