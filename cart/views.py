from django.shortcuts import render
from .cart import Cart
from products.models import Product

# Create your views here.

# cart object
def cart(request):

    return render(request, 'cart/cart.html')

# add to cart
def add(request, product_id):

    cart = Cart(request)

    cart.add(product_id)

    return render(request, 'cart/cart_menu.html')

# update cart
def hx_menu_cart(request):

    return render(request, 'cart/cart_menu.html')

# update cart
def hx_cart_total(request):

    return render(request, 'cart/cart_total.html')

# update cart
def update_cart(request, product_id, action):

    cart = Cart(request)

    if action == 'increment':

        cart.add(product_id, 1, True)

    else:

        cart.add(product_id, -1, True)

    product = Product.objects.get(pk=product_id)

    quantity = cart.get_item(product_id)['quantity']

    item = {
        'product': {
            'id': product.id,
            'product_name': product.product_name,
            'thumbnail': product.thumbnail,
            'price': product.price,
            'slug': product.slug,
        },
        'total_price': (quantity * product.price),
        'quantity': quantity,
    }

    response = render(request, 'cart/cart_item.html', {'item': item})

    response['HX-Trigger'] = 'update-cart-menu'

    return response