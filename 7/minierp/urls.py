
from django.conf.urls import patterns, include, url
from views import *

urlpatterns = patterns('',
    ('^$', index),
    ('^index/$', index),

    ('^product/list/$', product_list),
    ('^product/add/$', product_add),
    ('^product/del/(\w+)/$', product_del),
    ('^product/update/$', product_update),
    ('^product/export/product.csv$', product_export),

    ('^customer/list/$', customer_list),
    ('^customer/add/$', customer_add),
    ('^customer/del/(\w+)/$', customer_del),
    ('^customer/update/$', customer_update),
    ('^customer/info/(\w+)/$', customer_info),
    ('^customer/export/customer.csv$', customer_export),

    ('^supplier/list/$', supplier_list),
    ('^supplier/add/$', supplier_add),
    ('^supplier/del/(\w+)/$', supplier_del),
    ('^supplier/update/$', supplier_update),
    ('^supplier/info/(\w+)/$', supplier_info),
    ('^supplier/export/supplier.csv$', supplier_export),

    ('^stock/$', stock),
    ('^stock/export/stock.csv$', stock_export),

    ('^purchase/list/$', purchase_list),
    ('^purchase/add/$', purchase_add),
    ('^purchase/del/(\w+)/$', purchase_del),
    ('^purchase/export/purchase.csv$', purchase_export),

    ('^sale/list/$', sale_list),
    ('^sale/add/$', sale_add),
    ('^sale/del/(\w+)/$', sale_del),
    ('^sale/export/sale.csv$', sale_export),

    ('^loginpage/$', loginpage),
    ('^registerpage/$', registerpage),
    ('^login/$', login),
    ('^logout/$', logout),
    ('^register/$', register),

)

# This will work if DEBUG is True
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
