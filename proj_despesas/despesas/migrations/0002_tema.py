# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-15 19:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('despesas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('funcao', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tema',
                'managed': False,
            },
        ),
    ]
