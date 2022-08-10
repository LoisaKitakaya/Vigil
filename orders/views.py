from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from cart.cart import Cart

# Create your views here.

# checkout method
@login_required
def checkout_view(request):

    return render(request, 'orders/checkout.html')

# adding shipping cost
def add_shipping_cost(request, shipping_cost):

    cart = Cart(request)

    cart.get_total_cost(shipping_cost)

    return render(request, 'orders/checkout_total.html')