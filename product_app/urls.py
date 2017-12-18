from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index, name='index'),
    url(r'^(?P<stock_id>[0-9]+)/$', views.detail, name='detail'),
    # url('^stock-operation/', views.create_stock_operation, name='add_stock_operation'),
    url('^stock/', views.stock, name='add_stock'),
    url('^dashboard/$', views.dashboard, name='dashboard'),
    url('^stock-operations/', views.stock_operation, name='stock_operation')
]
