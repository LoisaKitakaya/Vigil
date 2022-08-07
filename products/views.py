from django.shortcuts import render, redirect
from .models import Product

# Create your views here.
def all_products(request):

    products = Product.objects.all()

    context = {
        'all_products': products,
    }

    return render(request, 'products/all_products.html', context)

def single_product(request, slug):

    product = Product.objects.get(slug=slug)

    context = {
        'this_product': product,
    }

    return render(request, 'products/product.html', context)