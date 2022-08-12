from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Order,OrderItem
from cart.cart import Cart
import string 
import random 

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

# create order
@login_required
def create_order(request):

    cart = Cart(request)

    if request.method == 'POST':

        user = request.user

        email = request.POST['email']

        first_name = request.POST['firstname']

        last_name = request.POST['lastname']

        address_1 = request.POST['address1']

        address_2 = request.POST['address2']

        postal_code = request.POST['postalcode']

        city = request.POST['city']

        place = request.POST['place']

        phone_number = request.POST['phone']

        delivery_method = request.POST['deliverymethod']

        N = 15

        res = ''.join(random.choices(string.ascii_uppercase +  string.digits, k = N))

        order = Order.objects.create(
            owner=user,
            order_uic=str(res),
            email=email,
            first_name=first_name,
            last_name=last_name,
            address=address_1,
            address_2=address_2,
            postal_code=postal_code,
            phone_number=phone_number,
            city=city,
            place=place,
            delivery_method=delivery_method
        )

        for item in cart:

            product = item['product']

            quantity = int(item['quantity'])

            price = product.price * quantity

            OrderItem.objects.create(
                order=order,
                product=product,
                price=price,
                quantity=quantity
            )

        messages.success(request, 'Your order has been created')

        return redirect('cart')

    return redirect('cart')
    