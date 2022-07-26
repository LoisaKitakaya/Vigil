from django.contrib import admin
from .models import ProductCategory, ProductInventory, ProductReview, ProductBrand, Product

# Register your models here.
@admin.register(ProductCategory)
class ProductCategoryAdminView(admin.ModelAdmin):

    model = ProductCategory

    list_display = (
        'name',
        'description',
    )

    list_filter = (
        'created_date',
        'updated_date',
    )

    prepopulated_fields = {"slug": ("name",)}

@admin.register(ProductInventory)
class ProductInventoryAdminView(admin.ModelAdmin):

    model = ProductInventory

    list_display = (
        'product',
        'quantity',
    )

    list_filter = (
        'created_date',
        'updated_date',
    )

@admin.register(ProductReview)
class ProductReviewAdminView(admin.ModelAdmin):

    model = ProductReview

    list_display = (
        'name',
        'rating',
        'review',
    )

    list_filter = (
        'created_date',
        'updated_date',
    )

@admin.register(ProductBrand)
class ProductBrandAdminView(admin.ModelAdmin):

    model = ProductBrand

    list_display = (
        'name',
        'description',
    )

    list_filter = (
        'created_date',
        'updated_date',
    )

    prepopulated_fields = {"slug": ("name",)}

@admin.register(Product)
class ProductAdminView(admin.ModelAdmin):

    model = Product

    list_display = (
        'name',
        'price',
        'product_category',
    )

    list_filter = (
        'created_date',
        'updated_date',
    )

    prepopulated_fields = {"slug": ("name",)}