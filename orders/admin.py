from django.contrib import admin
from .models import ShippingCost, Order, OrderItem

# Register your models here.
@admin.register(ShippingCost)
class ShippingCostAdminView(admin.ModelAdmin):

    model = ShippingCost

    list_display = (
        'shipping_cost',
    )

    list_filter = (
        'created_date',
        'updated_date'
    )

@admin.register(OrderItem)
class OrderItemAdminView(admin.ModelAdmin):

    model = OrderItem

    list_display = (
        'order',
        'product',
        'price',
        'quantity',
    )

    list_filter = (
        'created_date',
        'updated_date'
    )

@admin.register(Order)
class OrderAdminView(admin.ModelAdmin):

    model = Order

    list_display = (
        'order_uic',
        'owner',
        'status',
        'paid',
    )

    list_filter = (
        'owner',
        'paid',
        'status',
        'created_date',
        'updated_date',
    )