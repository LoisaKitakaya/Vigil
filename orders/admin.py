from django.contrib import admin
from .models import ShippingCost

# Register your models here.
@admin.register(ShippingCost)
class ShippingCostAdminView(admin.ModelAdmin):

    model = ShippingCost

    list_display = (
        'shipping_cost',
    )

    list_filter = (
        'created_date',
    )