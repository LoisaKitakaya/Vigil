from django.urls import path
from . import views

# your urls here
urlpatterns = [
    path('', views.all_products, name="all-products"),
    path('<slug:slug>/', views.single_product, name="single-product"),
]