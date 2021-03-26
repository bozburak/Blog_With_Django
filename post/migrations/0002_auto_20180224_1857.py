# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-24 15:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=1, upload_to=b''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(verbose_name='\u0130\xe7erik'),
        ),
        migrations.AlterField(
            model_name='post',
            name='publishing_date',
            field=models.DateTimeField(verbose_name='Yay\u0131nlanma Tarihi'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Ba\u015fl\u0131k'),
        ),
    ]