# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 23:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(blank=True, db_column='codigo', max_length=10, null=True)),
                ('nombre', models.CharField(blank=True, db_column='nombre', max_length=255, null=True)),
                ('precio', models.DecimalField(blank=True, db_column='precio', decimal_places=2, max_digits=9, null=True)),
                ('existencia', models.DecimalField(blank=True, db_column='existencia', decimal_places=3, max_digits=9, null=True)),
            ],
        ),
    ]
