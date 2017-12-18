# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

OPERATION_TYPE = [('stock_input', 'Stock Input'),
                  ('stock_output', 'Stock Output'),
                  ]


class Product(models.Model):
    product_id = models.CharField(max_length=20, null=True, unique=True)
    product_name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.product_name


class Location(models.Model):
    location_id = models.CharField(max_length=20, null=True, unique=True)
    location_name = models.CharField(max_length=128, null=True)

    def __str__(self):
        return self.location_name


class StockOperation(models.Model):
    location = models.ForeignKey('Location', on_delete=models.PROTECT)
    product = models.ForeignKey('Product', on_delete=models.PROTECT)
    quantity = models.IntegerField()
    operation_type = models.CharField(max_length=20, choices=OPERATION_TYPE)

    def __str__(self):
        return "{}-{}-{} :{}".format(self.product, self.location, self.operation_type, self.quantity)


class Stock(models.Model):
    location = models.ForeignKey('Location', on_delete=models.PROTECT)
    product = models.ForeignKey('Product', on_delete=models.PROTECT)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return "{}-{}: {}".format(self.product, self.location, self.quantity)
