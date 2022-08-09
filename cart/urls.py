from django.urls import path
from . import views

# your urls here
urlpatterns = [
    path('', views.cart, name='cart'),
    path('add/<int:product_id>/', views.add, name="add-product"),
]