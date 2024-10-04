from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore

from django.template import loader # type: ignore # this module helps load html template
from django.views.generic import ListView, CreateView   # type: ignore
from .models import Product
# Create your views here.

from django import forms # type: ignore

def home(request):
    products = Product.objects.all() # collecting all the products
    context = {
        'prods' : products,
        
    }
    template = loader.get_template('home.html')
    return HttpResponse(template.render(context, request))

def product_details(request, id):
    product = Product.objects.get(id = id)
    context = {
        'product' : product
    }
    template = loader.get_template('prod_details.html')
    return HttpResponse(template.render(context, request))

class ProductList(ListView):
    model = Product
    template_name = 'products.html'

def about(request):
    # return HttpResponse("Hi, this is my about page !!!")
    template = loader.get_template('about.html')
    return HttpResponse(template.render())

def addProduct(request):
    # return HttpResponse("Hi, this is my adding product page !!!")
    template = loader.get_template('addProduct.html')
    return HttpResponse(template.render())

class AddProduct(CreateView):
    model = Product
    template_name = "addProduct.html"
    fields = [
        'name',
        'price',
        'description',
        'stock',
        'pic'
    ]

    success_url = "/"
    
    # forms.py



