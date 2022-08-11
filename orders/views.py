from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from cart.cart import Cart

# Create your views here.

# checkout method
@login_required
def checkout_view(request):

    return render(request, 'orders/checkout.html')

# adding shipping cost
def hx_update_shipping(request):

    return render(request, 'orders/checkout_total.html')

# adding shipping cost
def update_shipping_cost(request, shipping_cost):

    cart = Cart(request)

    net_cost = cart.get_total_cost(shipping_cost)

    print(net_cost)

    new_total = {
        'get_total_cost': net_cost,
    }

    response = render(request, 'orders/checkout_total.html', {'cart': new_total})

    response['HX-Trigger'] = 'update-shipping-cost'

    return response

    