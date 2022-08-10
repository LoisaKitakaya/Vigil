from django.urls import path
from . import views

# your urls here
urlpatterns = [
    path('', views.checkout_view, name="checkout")
]