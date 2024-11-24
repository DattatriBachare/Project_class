from django.shortcuts import render, redirect
from .models import Product, CartItem

# Create your views here.

def viewCart(request):
    template = 'cart.html'
    cart_item = CartItem.objects.filter(user = request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_item)
    
    context = {
        'cart_item' : cart_item,
        'total_price' : total_price
    }
    return render(request, template , context)

def addToCart(request, product_id):
    this_product = Product.objects.get(id = product_id)
    cart_item, created = CartItem.objects.get_or_create(product = this_product, user = request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart:view_cart')
     