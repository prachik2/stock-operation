# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from silk.profiling.profiler import silk_profile
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from product_app.models import Stock, StockOperation
from .forms import StockForm, StockOperationForm


def index(request):
    print request

    return HttpResponse("Hello, world. You're at the index.")


def detail(request, stock_id):
    print request
    return HttpResponse("You're looking at stock_input %s." % stock_id)


# def create_stock_operation(request, template="single_input_stock.html"):
#     # import pdb;pdb.set_trace()
#     # current_stock = 10
#     if request.method == "POST":
#         stock_input_form = StockInputForm(request.POST)
#         if stock_input_form.is_valid():
#             print "Form Valid"
#             cleaned_data = stock_input_form.cleaned_data
#             stock_quantity = cleaned_data['quantity']
#             location = cleaned_data['location']
#             product = cleaned_data['product']
#             operation_type = cleaned_data['operation_type']
#
#             if operation_type == 'stock_input':
#                 stock_quantity = current_stock_input + int(stock_quantity)
#
#             elif operation_type == 'stock_output':
#                 stock_quantity = current_stock_output - int(stock_quantity)
#
#             stock_input = StockOperation.objects.create(quantity=stock_quantity, location=location, product=product, operation_type=operation_type)
#             print stock_input
#             stock_input.save()
#             print' stock input created'
#             print stock_quantity
#             print location
#             print product
#             print operation_type
#             # context = {
#             #     'quantity': stock_quantity,
#             #     'location': location,
#             #     'product': product,
#             #     'operation_type': operation_type,
#             # }
#             return HttpResponseRedirect(reverse('dashboard'))
#     else:
#         stock_input_form = StockInputForm()
#         # return HttpResponseRedirect(reverse('dashboard'))
#     return render(request, template, {'stock_input_form': stock_input_form})



def dashboard(request, template="dashboard.html"):
    if request.GET:
        print "Dashboard View"
        print request
        # stock_operations = StockOperation.objects.all()

    return render(request, template)



def stock(request, template="input_stock.html"):
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            location = form.cleaned_data['location']
            product = form.cleaned_data['product']
            quantity = form.cleaned_data['quantity']
            operation_type = form.cleaned_data['operation_type']

            stock_instance, created = Stock.objects.get_or_create(location=location, product=product, defaults={'quantity': 0})
            # print(dir(stock_instance))

            if operation_type == 'stock_input':
                stock_instance.quantity += quantity
                stock_instance.save()
            else:
                stock_instance.quantity -= quantity
                stock_instance.save()

            return HttpResponseRedirect(reverse('dashboard'))

    else:
        form = StockForm()
        return render(request, template, {'form': form})


@silk_profile(name='stock_operation')
def stock_operation(request, template="stock_operation.html"):
    if request.method == 'POST':
        form = StockOperationForm(request.POST)
        if form.is_valid():
            operation_instance = form.save(commit=False)
            print operation_instance.quantity
            if operation_instance.operation_type == 'stock_input':
                # print sum(operation_instance.quantity)
                operation_instance.quantity += operation_instance.quantity
            else:
                operation_instance.quantity = operation_instance.quantity
            operation_instance.save()
            print (dir(operation_instance))
            return HttpResponseRedirect(reverse('dashboard'))
    else:
        form = StockOperationForm()
    return render(request, template, {'form': form})


def updated_stocks(request, template="updated_stocks.html"):
    if request.method == 'GET':
        list_location_1 = []
        list_location_2 = []
        list_location_3 = []
        list_location_4 = []
        product_list = []

        all_stocks = StockOperation.objects.all()
        for product in all_stocks:
            if str(product.product) == 'Product 1'and str(product.location) == 'Location 1':
                list_location_1.append(product.quantity)
            if str(product.product) == 'Product 2'and str(product.location) == 'Location 1':
                list_location_2.append(product.quantity)
            if str(product.product) == 'Product 1'and str(product.location) == 'Location 2':
                list_location_3.append(product.quantity)
            if str(product.product) == 'Product 2'and str(product.location) == 'Location 2':
                list_location_4.append(product.quantity)
        print sum(list_location_2)
        print sum(list_location_1)
        print sum(list_location_3)
        print sum(list_location_4)



    return render(request, template ,{'list_location_1':sum(list_location_1),'list_location_2':sum(list_location_2),'list_location_3':sum(list_location_3),'list_location_4':sum(list_location_4) })

