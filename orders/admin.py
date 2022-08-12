from django.contrib import admin
from .models import ShippingCost, Order

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

@admin.register(Order)
class OrderAdminView(admin.ModelAdmin):

    model = Order

    list_display = (
        'order_uic',
        'paid_amount',
    )

    list_filter = (
        'owner',
        'paid',
        'status',
        'created_date',
        'updated_date',
    )