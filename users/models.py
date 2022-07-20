from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):

    email = models.EmailField(blank=False, max_length=254, verbose_name="email address", unique=True)

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"

    class Meta:

        db_table = "App Users"

class UserAddress(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="user")
    city = models.CharField(max_length=254, blank=False, verbose_name="City")
    address_one = models.CharField(max_length=254, blank=False, verbose_name="address 1")
    address_two = models.CharField(max_length=254, blank=False, verbose_name="address 2")
    primary_phone = models.CharField(max_length=254, blank=False, verbose_name="primary phone number")
    secondary_phone = models.CharField(max_length=254, blank=False, verbose_name="secondary phone number")

    class Meta:

        db_table = "User Addresses"

    def __str__(self) -> str:
        
        return f'User: {self.user}. City: {self.city}. Address: {self.address_one}. Phone: {self.primary_phone}'
