from django.urls import path
from . import views

# your urls here
urlpatterns = [
    path('', views.cart, name='cart'),
    path('add/<int:product_id>/', views.add, name="add-product"),
    path('hx_menu_cart/', views.hx_menu_cart, name="hx-menu-cart"),
    path('hx_cart_total', views.hx_cart_total, name="hx-cart-total"),
    path('update_cart/<int:product_id>/<str:action>/', views.update_cart, name="update-cart"),
    path('clear_cart/', views.clear_cart, name="clear-cart"),
]