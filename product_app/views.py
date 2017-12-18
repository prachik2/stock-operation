# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from .forms import StockInputForm
from .models import StockOperation


def index(request):
    print request
    return HttpResponse("Hello, world. You're at the index.")


def detail(request, stock_id):
    print request
    return HttpResponse("You're looking at stock_input %s." % stock_id)


def create_input_stock(request, template="single_input_stock.html"):
    # import pdb;pdb.set_trace()
    # form_class = StockInputForm
    # model = StockOperation
    # template = loader.get_template('single_input_stock.html')
    # template_name = 'single_input_stock.html'
    # success_url = '/stocks/stock-operations'
    # print request.url
    if request.method == "POST":
        stock_input_form = StockInputForm(request.POST)
        if stock_input_form.is_valid():
            print "Form Valid"
            cleaned_data = stock_input_form.cleaned_data
            stock_quantity = cleaned_data['quantity']
            location = cleaned_data['location']
            product = cleaned_data['product']
            operation_type = cleaned_data['operation_type']

            stock_input = StockOperation.objects.create(quantity=stock_quantity,location=location, product=product, operation_type=operation_type)
            print stock_input
            stock_input.save()
            print' stock input created'
            # context = {
            #     'quantity': stock_quantity,
            #     'location': location,
            #     'product': product,
            #     'operation_type': operation_type,
            # }
            return HttpResponseRedirect(reverse('dashboard'))
    else:
        stock_input_form = StockInputForm()
        # return HttpResponseRedirect(reverse('dashboard'))
    return render(request, template, {'stock_input_form': stock_input_form},)


def dashboard(request, template="dashboard.html"):
    if request.GET:
        print "Dashboard View"
        print request
    return render(request, template)
    #     def get(self, request, *args, **kwargs):
    #         self.object = self.get_object()
    #         context = self.get_context_data(object=self.object)
    #         try:
    #             return self.render_to_response(context)
    #         except:
    #             return HttpResponseRedirect(reverse("users:home"))
    #
    #             # return render(request, template)



