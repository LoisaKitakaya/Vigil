from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import messages
from .models import Product, ProductReview

# Create your views here.

# all products view
def all_products(request):

    products = Product.objects.all()

    context = {
        'all_products': products,
    }

    return render(request, 'products/all_products.html', context)

# single product view
def single_product(request, slug):

    if request.method == 'POST':

        user = request.user

        item_name = request.POST['productname']

        rating = request.POST['rating']

        review = request.POST['productreview']

        user_review = ProductReview.objects.create(
            user=user,
            item_name=item_name,
            rating=rating,
            review=review
        )

        product = Product.objects.get(slug=slug)

        product.product_review.add(user_review)

        messages.success(request, 'Your review has been posted.')

    product = Product.objects.get(slug=slug)

    context = {
        'this_product': product,
    }

    return render(request, 'products/product.html', context)

# category filter view
def category_filter(request, slug):

    category = Product.objects.filter(product_category__slug=slug)

    context = {
        'this_category': category,
        'category': slug,
    }

    return render(request, 'products/categories.html', context)

# tag filter view
def tag_filter(request, slug):

    tag = Product.objects.filter(product_tags__slug=slug)

    context = {
        'this_tag': tag,
        'tag': slug,
    }

    return render(request, 'products/tags.html', context)

# search filter view
def search_filter(request):

    if request.method == 'GET':

        query = request.GET['search']

        try:

            query_result = Product.objects.filter(
                Q(product_name__icontains=query) | 
                Q(full_name__icontains=query) | 
                Q(product_category__category_name__icontains=query)
            )

        except query_result.DoesNotExist:

            query_result = None

    context = {
        'query_results': query_result,
        'query_name': query, 
    }

    return render(request, 'products/search_results.html', context)