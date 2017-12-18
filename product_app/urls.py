from django.conf.urls import url
from .models import *
from . import views

urlpatterns = [
    url('^$', views.index, name='index'),
    url(r'^(?P<stock_id>[0-9]+)/$', views.detail, name='detail'),
    url('^stock-input/', views.create_input_stock, name='stock_input'),
    # url('stock_output/', views.create_output_stock, name='stock_output'),
    url('^dashboard/$', views.dashboard, name='dashboard'),

]
