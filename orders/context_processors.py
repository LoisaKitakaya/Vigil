from .models import ShippingCost

def delivery_cost(request):

    cost = ShippingCost.objects.get(pk=1)

    return {
        'delivery_cost': cost
    }

def pickup_cost(request):

    cost = ShippingCost.objects.get(pk=2)

    return {
        'pickup_cost': cost
    }