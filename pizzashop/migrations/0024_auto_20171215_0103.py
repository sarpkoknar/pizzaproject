# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-14 19:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzashop', '0023_auto_20171215_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='pizzashop/', verbose_name='Изображение'),
        ),
    ]
