from django.shortcuts import render 
from django.http import HttpResponse

from django.template import loader # type: ignore # this module helps load html template
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Product
from django.urls import reverse , reverse_lazy

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

def about(request):
    context = {        
    }
    template = loader.get_template('about.html')
    return HttpResponse(template.render(context, request))

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


class EditProduct(UpdateView):
    model = Product
    template_name = "EditProduct.html"
    fields = [
        'name',
        'price',
        'description',
        'stock',
        'pic'
    ]
    success_url = reverse_lazy('products') 
    
class DelProduct(DeleteView):
    model = Product
    template_name = "DelProduct.html"
    success_url = reverse_lazy('products')     
    
    
def searchView(request):
    query = request.GET.get('q1')
    results = Product.objects.filter(name__icontains=query) # filtering the products objects according string matching query 
    # In the SQL => select * from products where name like "%query%"
    context = {
        'prods' : results,
        'query' : query,
        
    }
    template = loader.get_template('search_results.html')
    return HttpResponse(template.render(context, request))

class ProductSearchView(ListView):
    model = Product
    template_name = 'search_results.html'
    context_object_name = 'prods'


# by default, this method of ListView collects all objects of the given class name
# we are overriding and altering the method to collect only the objects with name containing the search string
def get_queryset(self):
    query = self.request.GET.get('q1')
    if query:
        return Product.objects.filter(name__icontains=query)
    # This will 
    return Product.objects.all()

# overrides the method which provides the context data, 
# adds more key-value pairs to the dict and returns it
# this will alter the context data before sending for rendering with template


def get_context_data(self, **kwargs):
        default_context =  super().get_context_data(**kwargs) 
        # getting the default context variables using superclass method
        query = self.request.GET.get('q1','')
        default_context['query'] = query
        return default_context