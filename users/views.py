from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

# user registration
def register(request):

    if request.method == 'POST':

        username = request.POST['username']

        email = request.POST['email']

        password1 = request.POST['password1']

        password2 = request.POST['password2']

        if password1 == password2:

            User.objects.create(username=username, email=email)

            new_user = User.objects.get(email=email)

            new_user.set_password(password1)

            new_user.save()

            messages.success(request, 'Your account has been created')

            return redirect('login-user')

        else:

            messages.error(request, 'Passwords did not match')

    return render(request, 'users/register.html')

def sign_in(request):

    if request.method == 'POST':

        username = request.POST['username']

        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:

            login(request, user)

            messages.success(request, 'Logged in successfully')

            return redirect('all-products')

        else:
            
            messages.error(request, 'Provided username or password is incorrect')

    return render(request, 'users/sign_in.html')

def logout_view(request):

    logout(request)

    messages.success(request, 'Logged out successfully')

    return redirect('all-products')

