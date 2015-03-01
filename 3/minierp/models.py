# -*- coding: utf-8 -*-

from django.db import models

class Product(models.Model):
    pid = models.CharField(max_length=64, blank=True , null=True)
    name = models.CharField(max_length=128, blank=True , null=True)
    price = models.FloatField(default=0)


class Customer(models.Model):
    name = models.CharField(max_length=128, blank=True , null=True)
    phone = models.CharField(max_length=128, blank=True , null=True)
    email = models.CharField(max_length=128, blank=True , null=True)


class Supplier(models.Model):
    name = models.CharField(max_length=128, blank=True , null=True)
    phone = models.CharField(max_length=128, blank=True , null=True)
    email = models.CharField(max_length=128, blank=True , null=True)


class Stock(models.Model):
    product = models.ForeignKey(Product)
    quantity = models.IntegerField(default=0)

