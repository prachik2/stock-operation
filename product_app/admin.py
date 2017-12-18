# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from product_app.models import Product, Location, StockOperation

# Register your models here.
admin.site.register(Product)
admin.site.register(Location)
admin.site.register(StockOperation)
