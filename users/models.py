from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):

    email = models.EmailField(blank=False, max_length=254, verbose_name="email address", unique=True)

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"

    class Meta:

        db_table = "User Accounts"

class NewsletterSubscription(models.Model):

    email = models.EmailField(blank=False, max_length=254, verbose_name="subscription email", unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:

        ordering = ['-created_date']

        db_table = 'Newsletter Subscribers'

    def __str__(self) -> str:
        
        return self.email
