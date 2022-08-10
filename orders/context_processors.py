from .models import ShippingCost

def shipping_cost(request):

    cost = ShippingCost.objects.get(pk=1)

    return {
        'shipping_cost': cost
    }