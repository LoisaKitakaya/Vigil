from django.db import models
from users.models import User
from cloudinary.models import CloudinaryField
from django_quill.fields import QuillField

# Create your models here.
class ProductReview(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=254, blank=False, verbose_name="item name")
    rating = models.IntegerField(default=0, blank=False, verbose_name="item rating")
    review = models.TextField(verbose_name="item review")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:

        ordering = ["-created_date"]

        db_table = "Products Reviews"

    def __str__(self) -> str:
        
        return self.item_name

class ProductCategory(models.Model):

    category_name = models.CharField(max_length=254, blank=False, verbose_name="category name")
    slug = models.SlugField(max_length=254, blank=False, verbose_name="category slug")
    description = models.TextField(verbose_name="category description")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:

        ordering = ["created_date"]

        db_table = "Products Category"

    def __str__(self) -> str:
        
        return self.category_name

class ProductTag(models.Model):

    tag_name = models.CharField(max_length=254, blank=False, verbose_name='tag name')
    slug = models.SlugField(max_length=254, blank=False, verbose_name="tag slug")
    description = models.TextField(verbose_name="tag description")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:

        ordering = ["created_date"]

        db_table = "Product Tags"

    def __str__(self) -> str:
        
        return self.tag_name

class Product(models.Model):

    product_name = models.CharField(max_length=254, blank=False, verbose_name="product name", unique=True)
    full_name = models.CharField(max_length=254, blank=False, verbose_name="product full name")
    slug = models.SlugField(max_length=254, blank=False, verbose_name="product slug")
    price = models.FloatField(default=0, verbose_name="product price")
    thumbnail = CloudinaryField('thumbnail')
    description = QuillField()
    slide_one = CloudinaryField('slide_one')
    slide_two = CloudinaryField('slide_two')
    slide_three = CloudinaryField('slide_three')
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    product_tags = models.ManyToManyField(ProductTag)
    product_review = models.ManyToManyField(ProductReview)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:

        ordering = ['-created_date']

        db_table = "Products Table"

    def __str__(self) -> str:
        
        return self.product_name

class ProductInventory(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, verbose_name="product quantity")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:

        ordering = ["created_date"]

        db_table = "Products Inventory"

    def __str__(self) -> str:
        
        return str(self.quantity)