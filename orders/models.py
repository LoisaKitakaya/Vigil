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

        db_table = "Shipping Cost"

    def __str__(self) -> str:
        
        return self.delivery_method

