from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):

    email = models.EmailField(blank=False, max_length=254, verbose_name="email address", unique=True)

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"

    class Meta:

        db_table = "App Users"

class Address(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=254, blank=False, verbose_name="city of residence")
    address = models.CharField(max_length=254, blank=False, verbose_name="address 1")
    phone_one = models.CharField(max_length=254, blank=False, verbose_name="primary phone")
    phone_two = models.CharField(max_length=254, blank=False, verbose_name="secondary phone")

    class Meta:

        db_table = "User Addresses"

    def __str__(self) -> str:
        
        return f'User: {self.user}. City: {self.city}. Address: {self.address}. Phone: {self.phone_one}.'
