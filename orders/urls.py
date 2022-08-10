from django.urls import path
from . import views

# your urls here
urlpatterns = [
    path('', views.checkout_view, name="checkout"),
    path('add_shipping/<int:shipping_cost>/', views.add_shipping_cost, name="add-shipping-cost"),
]