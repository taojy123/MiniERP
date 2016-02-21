# -*- coding: utf-8 -*-

from django.db import models

class Product(models.Model):
    pid = models.CharField(max_length=64, blank=True , null=True)
    name = models.CharField(max_length=128, blank=True , null=True)
    price = models.FloatField(default=0)
