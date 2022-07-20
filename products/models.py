from django.db import models

# Create your models here.

# class ProductDiscount(models.Model):

#     name = models.CharField(max_length=254, blank=False, verbose_name="discount name")
#     discount_percent = models.FloatField(default=0.0, verbose_name="discount percentage")
#     created_date = models.DateTimeField(auto_now_add=True)
#     updated_date = models.DateTimeField(auto_now=True)

#     class Meta:

#         ordering = ['created_date']

#         db_table = "Products Discount"

#     def __str__(self) -> str:
        
#         return f'Sale: {self.name}. Discount: {self.discount_percent}.'

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
        
        return f'Category: {self.name}.'

class Product(models.Model):

    name = models.CharField(max_length=254, blank=False, verbose_name="product name")
    slug = models.SlugField(max_length=254, blank=False, verbose_name="product slug")
    price = models.IntegerField(default=0, verbose_name="product price")
    thumbnail = models.URLField(max_length=254, blank=False, verbose_name="product thumbnail")
    description = models.TextField(verbose_name="describe the product")
    slide_one = models.URLField(max_length=254, blank=False, verbose_name="product slide 1")
    slide_two = models.URLField(max_length=254, blank=False, verbose_name="product slide 2")
    slide_three = models.URLField(max_length=254, blank=False, verbose_name="product slide 3")
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:

        ordering = ['created_date']

        db_table = "Products Table"

    def __str__(self) -> str:
        
        return f'Product: {self.name}. Price: {self.price}.'

class ProductInventory(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, verbose_name="quantity of product")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:

        ordering = ["created_date"]

        db_table = "Products Inventory"

    def __str__(self) -> str:
        
        return f'Stock quantity: {self.quantity}.'
