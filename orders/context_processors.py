from .models import ShippingCost

def delivery_cost(request):

    cost = ShippingCost.objects.filter(requires_payment=True).first()

    return {
        'delivery_cost': cost
    }

def pickup_cost(request):

    cost = ShippingCost.objects.filter(requires_payment=False).first()

    return {
        'pickup_cost': cost
    }