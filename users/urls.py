from django.urls import path
from . import views

# urls here
urlpatterns = [
    path('register/', views.register, name="register-account"),
    path('sign_in/', views.sign_in, name="login-user"),
]