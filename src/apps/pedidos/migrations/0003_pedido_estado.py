# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-05 06:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0002_auto_20180304_2051'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='estado',
            field=models.CharField(default='Pagado', max_length=400, verbose_name='Estado'),
            preserve_default=False,
        ),
    ]
