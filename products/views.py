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

def category_filter(request, slug):

    category = Product.objects.filter(product_category__slug=slug)

    context = {
        'this_category': category,
    }

    return render(request, 'products/categories.html', context)

def tag_filter(request, slug):

    tag = Product.objects.filter(product_tags__slug=slug)

    context = {
        'this_tag': tag,
    }

    return render(request, 'products/tags.html', context)