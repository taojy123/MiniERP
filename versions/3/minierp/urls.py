
from django.conf.urls import patterns, include, url
from views import *

urlpatterns = patterns('',
    ('^$', index),
    ('^index/$', index),

    ('^product/list/$', product_list),
    ('^product/add/$', product_add),
    ('^product/del/(\w+)/$', product_del),
    ('^product/update/$', product_update),

    ('^customer/list/$', customer_list),
    ('^customer/add/$', customer_add),
    ('^customer/del/(\w+)/$', customer_del),
    ('^customer/update/$', customer_update),

    ('^supplier/list/$', supplier_list),
    ('^supplier/add/$', supplier_add),
    ('^supplier/del/(\w+)/$', supplier_del),
    ('^supplier/update/$', supplier_update),

    ('^stock/$', stock),
    ('^stock/export/stock.csv$', stock_export),
)

# This will work if DEBUG is True
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
