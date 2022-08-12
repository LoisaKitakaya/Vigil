from django.urls import path
from . import views

# your urls here
urlpatterns = [
    path('', views.checkout_view, name="checkout"),
    path('update_shipping/<int:shipping_cost>/', views.update_shipping_cost, name="update-shipping-cost"),
    path('create_order/', views.create_order, name="create-order"),
]