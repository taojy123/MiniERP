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


# ======== Product CRUD =====================
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
    product.price = float(price)
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
    product.price = float(price)
    product.save()
    return HttpResponseRedirect("/product/list/")


# ======== Customer CRUD =====================
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


# ======== Supplier CRUD =====================
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


# ======== Stock =====================
def stock(request):
    stocks = Stock.objects.all()
    return render_to_response('stock.html', locals())

def stock_export(request):
    stocks = Stock.objects.all()
    return render_to_response('stock.csv', locals(), mimetype="application/octet-stream")


