from django.shortcuts import render
from .cart import Cart

# Create your views here.

# cart object
def cart(request):

    return render(request, 'cart/cart.html')

# add to cart
def add(request, product_id):

    cart = Cart(request)

    cart.add(product_id)

    return render(request, 'cart/cart_menu.html')