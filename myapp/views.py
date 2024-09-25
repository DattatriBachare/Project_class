from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore

from django.template import loader # type: ignore # this module helps load html template

from .models import Product
# Create your views here.


def home(request):
    products = Product.objects.all() # collecting all the products
    context = {
        'prods' : products,
        
    }
    template = loader.get_template('home.html')
    return HttpResponse(template.render(context, request))

def about(request):
    # return HttpResponse("Hi, this is my about page !!!")
    template = loader.get_template('about.html')
    return HttpResponse(template.render())
def addProduct(request):
    # return HttpResponse("Hi, this is my adding product page !!!")
    template = loader.get_template('addProduct.html')
    return HttpResponse(template.render())
