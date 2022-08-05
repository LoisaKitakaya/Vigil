from django.contrib import admin
from .models import ProductCategory, ProductInventory, ProductReview, ProductBrand, Product

# Register your models here.
@admin.register(ProductCategory)
class ProductCategoryAdminView(admin.ModelAdmin):

    model = ProductCategory

    list_display = (
        'category_name',
        'description',
    )

    list_filter = (
        'created_date',
        'updated_date',
    )

    prepopulated_fields = {"slug": ("category_name",)}

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
        'item_name',
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
        'brand_name',
        'description',
    )

    list_filter = (
        'created_date',
        'updated_date',
    )

    prepopulated_fields = {"slug": ("brand_name",)}

@admin.register(Product)
class ProductAdminView(admin.ModelAdmin):

    model = Product

    list_display = (
        'product_name',
        'price',
        'product_category',
    )

    list_filter = (
        'created_date',
        'updated_date',
    )

    prepopulated_fields = {"slug": ("product_name",)}