# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from models import *
import os
import uuid

def index(request):
    return render_to_response('index.html', locals())


# ======== Product =====================
@login_required(login_url="/loginpage")
def product_list(request):
    products = Product.objects.all()
    return render_to_response('product_list.html', locals())

@login_required(login_url="/loginpage")
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

@login_required(login_url="/loginpage")
def product_del(request, id):
    Product.objects.filter(id=id).delete()
    return HttpResponseRedirect("/product/list/")

@login_required(login_url="/loginpage")
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

@login_required(login_url="/loginpage")
def product_export(request):
    products = Product.objects.all()
    return render_to_response('product.csv', locals(), mimetype="application/octet-stream")


# ======== Customer =====================
@login_required(login_url="/loginpage")
def customer_list(request):
    customers = Customer.objects.all()
    return render_to_response('customer_list.html', locals())

@login_required(login_url="/loginpage")
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

@login_required(login_url="/loginpage")
def customer_del(request, id):
    Customer.objects.filter(id=id).delete()
    return HttpResponseRedirect("/customer/list/")

@login_required(login_url="/loginpage")
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

@login_required(login_url="/loginpage")
def customer_info(request, id):
    customer = Customer.objects.get(id=id)
    return render_to_response('customer_info.html', locals())

@login_required(login_url="/loginpage")
def customer_export(request):
    customers = Customer.objects.all()
    return render_to_response('customer.csv', locals(), mimetype="application/octet-stream")


# ======== Supplier =====================
@login_required(login_url="/loginpage")
def supplier_list(request):
    suppliers = Supplier.objects.all()
    return render_to_response('supplier_list.html', locals())

@login_required(login_url="/loginpage")
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

@login_required(login_url="/loginpage")
def supplier_del(request, id):
    Supplier.objects.filter(id=id).delete()
    return HttpResponseRedirect("/supplier/list/")

@login_required(login_url="/loginpage")
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

@login_required(login_url="/loginpage")
def supplier_info(request, id):
    supplier = Supplier.objects.get(id=id)
    return render_to_response('supplier_info.html', locals())

@login_required(login_url="/loginpage")
def supplier_export(request):
    suppliers = Supplier.objects.all()
    return render_to_response('supplier.csv', locals(), mimetype="application/octet-stream")


# ======== Stock =====================
@login_required(login_url="/loginpage")
def stock(request):
    stocks = Stock.objects.exclude(quantity=0)
    return render_to_response('stock.html', locals())

@login_required(login_url="/loginpage")
def stock_export(request):
    stocks = Stock.objects.exclude(quantity=0)
    return render_to_response('stock.csv', locals(), mimetype="application/octet-stream")


# ======== Purchase =====================
@login_required(login_url="/loginpage")
def purchase_list(request):
    purchases = Purchase.objects.all()
    products = Product.objects.all()
    suppliers = Supplier.objects.all()
    return render_to_response('purchase_list.html', locals())

@login_required(login_url="/loginpage")
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

@login_required(login_url="/loginpage")
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

@login_required(login_url="/loginpage")
def purchase_export(request):
    purchases = Purchase.objects.all()
    return render_to_response('purchase.csv', locals(), mimetype="application/octet-stream")



# ======== Sale =====================
@login_required(login_url="/loginpage")
def sale_list(request):
    sales = Sale.objects.all()
    products = Product.objects.all()
    customers = Customer.objects.all()
    return render_to_response('sale_list.html', locals())

@login_required(login_url="/loginpage")
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

@login_required(login_url="/loginpage")
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

@login_required(login_url="/loginpage")
def sale_export(request):
    sales = Sale.objects.all()
    return render_to_response('sale.csv', locals(), mimetype="application/octet-stream")



#==================== auth ===========================================
def loginpage(request):
    return render_to_response('loginpage.html', locals())

def registerpage(request):
    return render_to_response('registerpage.html', locals())

def login(request):
    username = request.REQUEST.get('username', '')
    password = request.REQUEST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
    return HttpResponseRedirect("/")

def logout(request):
    if request.user.is_authenticated():
        auth.logout(request)
    return HttpResponseRedirect("/")

def register(request):
    msg = ""
    username = request.REQUEST.get('username')
    password1 = request.REQUEST.get('password1')
    password2 = request.REQUEST.get('password2')
    if username and password1 and password2:
        if User.objects.filter(username=username):
            msg = "The user name is already registered"
            return render_to_response('registerpage.html', locals())
        if password1 == password2:
            user = User()
            user.username = username
            user.set_password(password1)
            user.save()
            return HttpResponseRedirect("/")
    msg = "You make a mistake, please re-enter"
    return render_to_response('registerpage.html', locals())



