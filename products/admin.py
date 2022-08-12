from django.contrib import admin
from .models import ProductTag, ProductCategory, ProductInventory, ProductReview, Product

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
        'review',
    )

    list_filter = (
        'rating',
        'created_date',
        'updated_date',
    )

@admin.register(ProductTag)
class ProductTagsAdminView(admin.ModelAdmin):

    model = ProductTag

    list_display = (
        'tag_name',
        'description',
    )

    list_filter = (
        'created_date',
        'updated_date',
    )

    prepopulated_fields = {"slug": ("tag_name",)}

@admin.register(Product)
class ProductAdminView(admin.ModelAdmin):

    model = Product

    list_display = (
        'product_name',
        'price',
    )

    list_filter = (
        'product_category',
        'created_date',
        'updated_date',
    )

    prepopulated_fields = {"slug": ("product_name",)}