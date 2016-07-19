# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-26 18:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cityscore', '0003_auto_20160626_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name=b'user'),
        ),
        migrations.AlterField(
            model_name='metric',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cityscore.City', verbose_name=b'city'),
        ),
        migrations.AlterField(
            model_name='value',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cityscore.City', verbose_name=b'city'),
        ),
        migrations.AlterField(
            model_name='value',
            name='metric',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cityscore.Metric', verbose_name=b'metric'),
        ),
    ]