from django.shortcuts import render, redirect
from users.models import NewsletterSubscription

# Create your views here.
def home(request):

    return render(request, 'core/home.html')

def subscribe(request):

    if request.method == 'POST':

        submitted_email = request.POST['newsletter']

        NewsletterSubscription.objects.create(email=submitted_email)

        return redirect('subscribe')

    return render(request, 'core/subscribe_success.html')