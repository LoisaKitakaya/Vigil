from django.contrib import admin
from .models import CartItem, DeliveryOrder, PickupOrder

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

@admin.register(DeliveryOrder)
class DeliveryOrderAdminView(admin.ModelAdmin):

    model = DeliveryOrder

    list_display = (
        'user',
        'order_uic',
        'total',
        'approved',
        'fulfilled',
    )

    list_filter = (
        'created_date',
    )

@admin.register(PickupOrder)
class PickupOrderAdminView(admin.ModelAdmin):

    model = PickupOrder

    list_display = (
        'user',
        'order_uic',
        'total',
        'approved',
        'fulfilled',
    )

    list_filter = (
        'created_date',
    )