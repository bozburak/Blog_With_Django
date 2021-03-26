# -*-coding:utf-8-*-
from __future__ import unicode_literals

from django.db import models

class Post(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=100, verbose_name="Başlık")
    content = models.TextField(verbose_name="İçerik")
    publishing_date = models.DateTimeField(verbose_name="Yayınlanma Tarihi")