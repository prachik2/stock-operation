# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from product_app.models import Product, Location, StockOperation, Stock
# from product_app.forms import StockOperationForm


# Register your models here.
admin.site.register(Product)
admin.site.register(Location)
admin.site.register(StockOperation)
admin.site.register(Stock)
