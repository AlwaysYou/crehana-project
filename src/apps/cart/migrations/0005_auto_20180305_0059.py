# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-05 00:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_item_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='unit_price',
            field=models.DecimalField(decimal_places=2, max_digits=18, verbose_name='Precio'),
        ),
    ]