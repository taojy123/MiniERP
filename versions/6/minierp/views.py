# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from models import *
import os
import uuid

def index(request):
    return render_to_response('index.html', locals())


# ======== Product =====================
def product_list(request):
    products = Product.objects.all()
    return render_to_response('product_list.html', locals())

def product_add(request):
    pid = request.POST.get("pid")
    name = request.POST.get("name")
    price = request.POST.get("price")
    product = Product()
    product.pid = pid
    product.name = name
    product.price = price
    product.save()
    return HttpResponseRedirect("/product/list/")

def product_del(request, id):
    Product.objects.filter(id=id).delete()
    return HttpResponseRedirect("/product/list/")

def product_update(request):
    id = request.POST.get("id")
    pid = request.POST.get("pid")
    name = request.POST.get("name")
    price = request.POST.get("price")
    product = Product.objects.get(id=id)
    product.pid = pid
    product.name = name
    product.price = price
    product.save()
    return HttpResponseRedirect("/product/list/")

def product_export(request):
    products = Product.objects.all()
    return render_to_response('product.csv', locals(), mimetype="application/octet-stream")


# ======== Customer =====================
def customer_list(request):
    customers = Customer.objects.all()
    return render_to_response('customer_list.html', locals())

def customer_add(request):
    name = request.POST.get("name")
    phone = request.POST.get("phone")
    email = request.POST.get("email")
    customer = Customer()
    customer.name = name
    customer.phone = phone
    customer.email = email
    customer.save()
    return HttpResponseRedirect("/customer/list/")

def customer_del(request, id):
    Customer.objects.filter(id=id).delete()
    return HttpResponseRedirect("/customer/list/")

def customer_update(request):
    id = request.POST.get("id")
    name = request.POST.get("name")
    phone = request.POST.get("phone")
    email = request.POST.get("email")
    customer = Customer.objects.get(id=id)
    customer.name = name
    customer.phone = phone
    customer.email = email
    customer.save()
    return HttpResponseRedirect("/customer/list/")

def customer_export(request):
    customers = Customer.objects.all()
    return render_to_response('customer.csv', locals(), mimetype="application/octet-stream")


# ======== Supplier =====================
def supplier_list(request):
    suppliers = Supplier.objects.all()
    return render_to_response('supplier_list.html', locals())

def supplier_add(request):
    name = request.POST.get("name")
    phone = request.POST.get("phone")
    email = request.POST.get("email")
    supplier = Supplier()
    supplier.name = name
    supplier.phone = phone
    supplier.email = email
    supplier.save()
    return HttpResponseRedirect("/supplier/list/")

def supplier_del(request, id):
    Supplier.objects.filter(id=id).delete()
    return HttpResponseRedirect("/supplier/list/")

def supplier_update(request):
    id = request.POST.get("id")
    name = request.POST.get("name")
    phone = request.POST.get("phone")
    email = request.POST.get("email")
    supplier = Supplier.objects.get(id=id)
    supplier.name = name
    supplier.phone = phone
    supplier.email = email
    supplier.save()
    return HttpResponseRedirect("/supplier/list/")

def supplier_export(request):
    suppliers = Supplier.objects.all()
    return render_to_response('supplier.csv', locals(), mimetype="application/octet-stream")


# ======== Stock =====================
def stock(request):
    stocks = Stock.objects.exclude(quantity=0)
    return render_to_response('stock.html', locals())

def stock_export(request):
    stocks = Stock.objects.exclude(quantity=0)
    return render_to_response('stock.csv', locals(), mimetype="application/octet-stream")


# ======== Purchase =====================
def purchase_list(request):
    purchases = Purchase.objects.all()
    products = Product.objects.all()
    suppliers = Supplier.objects.all()
    return render_to_response('purchase_list.html', locals())

def purchase_add(request):
    product_id = request.POST.get("product_id")
    supplier_id = request.POST.get("supplier_id")
    quantity = request.POST.get("quantity")
    product = Product.objects.get(id=product_id)
    supplier = Supplier.objects.get(id=supplier_id)
    purchase = Purchase()
    purchase.product = product
    purchase.supplier = supplier
    purchase.quantity = quantity
    purchase.save()
    qs = Stock.objects.filter(product=product)
    if qs:
        stock = qs[0]
    else:
        stock = Stock()
        stock.product = product
        stock.quantity = 0
    stock.quantity += int(quantity)
    stock.save()
    return HttpResponseRedirect("/purchase/list/")

def purchase_del(request, id):
    purchase = Purchase.objects.get(id=id)
    qs = Stock.objects.filter(product=purchase.product)
    if qs:
        stock = qs[0]
    else:
        stock = Stock()
        stock.product = purchase.product
        stock.quantity = 0
    stock.quantity -= purchase.quantity
    stock.save()
    purchase.delete()
    return HttpResponseRedirect("/purchase/list/")

def purchase_export(request):
    purchases = Purchase.objects.all()
    return render_to_response('purchase.csv', locals(), mimetype="application/octet-stream")



# ======== Sale =====================
def sale_list(request):
    sales = Sale.objects.all()
    products = Product.objects.all()
    customers = Customer.objects.all()
    return render_to_response('sale_list.html', locals())

def sale_add(request):
    product_id = request.POST.get("product_id")
    customer_id = request.POST.get("customer_id")
    quantity = request.POST.get("quantity")
    product = Product.objects.get(id=product_id)
    customer = Customer.objects.get(id=customer_id)
    sale = Sale()
    sale.product = product
    sale.customer = customer
    sale.quantity = quantity
    sale.save()
    qs = Stock.objects.filter(product=product)
    if qs:
        stock = qs[0]
    else:
        stock = Stock()
        stock.product = product
        stock.quantity = 0
    stock.quantity -= int(quantity)
    stock.save()
    return HttpResponseRedirect("/sale/list/")

def sale_del(request, id):
    sale = Sale.objects.get(id=id)
    qs = Stock.objects.filter(product=sale.product)
    if qs:
        stock = qs[0]
    else:
        stock = Stock()
        stock.product = sale.product
        stock.quantity = 0
    stock.quantity += sale.quantity
    stock.save()
    sale.delete()
    return HttpResponseRedirect("/sale/list/")

def sale_export(request):
    sales = Sale.objects.all()
    return render_to_response('sale.csv', locals(), mimetype="application/octet-stream")


