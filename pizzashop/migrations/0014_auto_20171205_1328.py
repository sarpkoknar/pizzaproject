# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-05 07:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizzashop', '0013_auto_20171205_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basketitem',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pizzashop.Order'),
        ),
    ]