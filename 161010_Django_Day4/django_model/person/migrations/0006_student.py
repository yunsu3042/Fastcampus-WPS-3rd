# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-10 01:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0005_computer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='person.Person')),
                ('year', models.CharField(max_length=20)),
            ],
            bases=('person.person',),
        ),
    ]