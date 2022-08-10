from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

# checkout method
@login_required
def checkout_view(request):

    return render(request, 'orders/checkout.html')