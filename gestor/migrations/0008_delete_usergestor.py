# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-24 12:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestor', '0007_usergestor_perfil_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserGestor',
        ),
    ]
