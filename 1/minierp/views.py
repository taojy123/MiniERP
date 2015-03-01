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


