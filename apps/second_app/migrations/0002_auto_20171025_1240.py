# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 19:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('second_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='second_friend',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='second', to='login_app.User'),
        ),
        migrations.AlterField(
            model_name='friend',
            name='user_friend',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='first', to='login_app.User'),
        ),
    ]
