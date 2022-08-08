from django.shortcuts import render, redirect
# from users.models import NewsletterSubscription

# Create your views here.
def home(request):

    return render(request, 'core/home.html')

# def subscribe(request):

#     if request.method == 'POST':

#         submitted_email = request.POST['newsletter']

#         current_user = request.user

#         NewsletterSubscription.objects.create(user=current_user, email=submitted_email)