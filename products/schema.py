import graphene
from graphene_django import DjangoObjectType
from .models import Product, ProductCategory, ProductInventory

# Your schema here
class ProductObject(DjangoObjectType):

    class Meta:

        model = Product

        fields = '__all__'

class ProductCategoryObject(DjangoObjectType):

    class Meta:

        model = ProductCategory

        fields = '__all__'

class ProductInventoryObject(DjangoObjectType):

    class Meta:

        model = ProductInventory

        fields = '__all__'

class Query(graphene.ObjectType):

    all_products = graphene.List(ProductObject)
    all_categories = graphene.List(ProductCategoryObject)
    all_inventory = graphene.List(ProductInventoryObject)

    single_product = graphene.Field(ProductObject, slug=graphene.String(required=True))
    single_category = graphene.List(ProductObject, slug=graphene.String(required=True))

    # resolving queries
    def resolve_all_products(root, info):

        return Product.objects.all()

    def resolve_all_categories(root, info):

        return ProductCategory.objects.all()

    def resolve_all_inventory(root, info):

        return ProductInventory.objects.all()

    def resolve_single_product(root, info, slug):

        return Product.objects.get(slug=slug)

    def resolve_single_category(root, info, slug):

        return Product.objects.filter(product_category__slug=slug)