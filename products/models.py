from django.db import models
from users.models import User

# Create your models here.
class ProductReview(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=254, blank=False, verbose_name="item name")
    rating = models.IntegerField(default=0, blank=False, verbose_name="item rating")
    review = models.TextField(verbose_name="item review")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:

        ordering = ["-created_date"]

        db_table = "Products Reviews"

    def __str__(self) -> str:
        
        return self.name

class ProductCategory(models.Model):

    name = models.CharField(max_length=254, blank=False, verbose_name="category name")
    slug = models.SlugField(max_length=254, blank=False, verbose_name="category slug")
    description = models.TextField(verbose_name="describe the category")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:

        ordering = ["created_date"]

        db_table = "Products Category"

    def __str__(self) -> str:
        
        return self.name

class ProductBrand(models.Model):

    name = models.CharField(max_length=254, blank=False, verbose_name="brand name")
    slug = models.SlugField(max_length=254, blank=False, verbose_name="brand slug")
    description = models.TextField(verbose_name="describe the brand")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:

        ordering = ["created_date"]

        db_table = "Products Brand"

    def __str__(self) -> str:
        
        return self.name

class Product(models.Model):

    name = models.CharField(max_length=254, blank=False, verbose_name="product name", unique=True)
    full_name = models.CharField(max_length=254, blank=False, verbose_name="product full name")
    slug = models.SlugField(max_length=254, blank=False, verbose_name="product slug")
    price = models.FloatField(default=0, verbose_name="product price")
    thumbnail = models.URLField(max_length=254, blank=False, verbose_name="product thumbnail")
    description = models.TextField(verbose_name="describe the product")
    specifications = models.TextField(verbose_name="specifications of the product")
    slide_one = models.URLField(max_length=254, blank=False, verbose_name="product slide 1")
    slide_two = models.URLField(max_length=254, blank=False, verbose_name="product slide 2")
    slide_three = models.URLField(max_length=254, blank=False, verbose_name="product slide 3")
    product_brand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE)
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    product_review = models.ManyToManyField(ProductReview)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:

        ordering = ['-created_date']

        db_table = "Products Table"

    def __str__(self) -> str:
        
        return self.name

class ProductInventory(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, verbose_name="quantity of product")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:

        ordering = ["created_date"]

        db_table = "Products Inventory"

    def __str__(self) -> str:
        
        return str(self.quantity)