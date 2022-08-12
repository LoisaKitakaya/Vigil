from django.db import models
from users.models import User

# Create your models here.
class ShippingCost(models.Model):

    delivery_method = models.CharField(max_length=254, blank=False, verbose_name="delivery method")
    shipping_cost = models.IntegerField(default=0, blank=False, verbose_name="shipping cost")
    requires_payment = models.BooleanField(default=True, verbose_name="payment needed")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:

        ordering = ['-created_date']

        db_table = "Shipping Costs"

    def __str__(self) -> str:
        
        return self.delivery_method

class Order(models.Model):

    ORDERED = 'ordered'
    SHIPPED = 'shipped'
    PICKED = 'picked'

    STATUS_CHOICES = (
        (ORDERED, 'Ordered'),
        (SHIPPED, 'Shipped'),
        (PICKED, 'Picked')
    )

    owner = models.ForeignKey(User, related_name="orders", on_delete=models.CASCADE)
    order_uic = models.CharField(max_length=254, blank=False, verbose_name="unique ID code")
    email = models.EmailField(max_length=254, blank=False, verbose_name="email")
    first_name = models.CharField(max_length=254, blank=False, verbose_name="first name")
    last_name = models.CharField(max_length=254, blank=False, verbose_name="last name")
    address = models.CharField(max_length=254, blank=False, verbose_name="address")
    address_2 = models.CharField(max_length=254, blank=True, null=True, verbose_name="address two")
    postal_code = models.CharField(max_length=254, blank=True, null=True, verbose_name="postal code")
    phone_number = models.CharField(max_length=254, blank=False, verbose_name="phone number")
    city = models.CharField(max_length=254, blank=False, verbose_name="city of residence")
    place = models.CharField(max_length=254, blank=False, verbose_name="place of residence")
    delivery_method = models.CharField(max_length=254, blank=False, verbose_name="delivery method")
    paid = models.BooleanField(default=False, verbose_name="paid")
    paid_amount = models.FloatField(default=0, blank=False, verbose_name="total payable")
    status = models.CharField(max_length=254, choices=STATUS_CHOICES, default=ORDERED, verbose_name="order status")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:

        ordering = ['-created_date']

        db_table = "Orders Table"

    def __str__(self) -> str:
        
        return self.owner


