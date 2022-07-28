from django.contrib import admin
from .models import CartItem, Order

# Register your models here.
@admin.register(CartItem)
class CartItemAdminView(admin.ModelAdmin):

    model = CartItem

    list_display = (
        'name',
        'quantity',
        'price',
    )

    list_filter = (
        'created_date',
    )

@admin.register(Order)
class OrderAdminView(admin.ModelAdmin):

    model = Order

    list_display = (
        'user',
        'order_uic',
        'total',
        'approved',
        'shipped',
    )

    list_filter = (
        'created_date',
    )