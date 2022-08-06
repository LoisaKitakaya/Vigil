from django.shortcuts import render, redirect

# Create your views here.
def all_products(request):

    return render(request, 'products/all_products.html')