from django.db import models
from users.models import User

# Create your models here.
class CartItem(models.Model):

    name = models.CharField(max_length=254, blank=False, verbose_name="product name")
    price = models.FloatField(default=0, verbose_name="product price")
    thumbnail = models.URLField(max_length=254, blank=False, verbose_name="product thumbnail")
    quantity = models.IntegerField(default=1, verbose_name="number of items")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:

        ordering = ['created_date']

        db_table = "Cart Items"

    def __str__(self) -> str:
        
        return f'Product: {self.name}. Price: {self.price}.'

class Order(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="owner of order")
    city = models.CharField(max_length=254, blank=False, verbose_name="city of residence")
    address = models.CharField(max_length=254, blank=False, verbose_name="address 1")
    phone_one = models.CharField(max_length=254, blank=False, verbose_name="primary phone")
    phone_two = models.CharField(max_length=254, blank=False, verbose_name="secondary phone")
    order_uic = models.CharField(max_length=254, blank=False, verbose_name="order unique identification code")
    item = models.ManyToManyField(CartItem)
    total = models.FloatField(default=0, blank=False, verbose_name="total payable")
    approved = models.BooleanField(default=False, verbose_name="approved for shipping")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:

        ordering = ['created_date']

        db_table = "Order Table"

    def __str__(self) -> str:
        
        return f'User: {self.user}. Order UIC: {self.order_uic}. Total: {self.total}. Approved: {self.approved}.'

