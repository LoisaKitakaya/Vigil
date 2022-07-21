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

    # resolving queries
    def resolve_all_products(root, info):

        user = info.context.user

        if not user.is_authenticated:

            raise Exception("Authentication credentials were not provided")

        else:

            return Product.objects.all()

    def resolve_all_categories(root, info):

        user = info.context.user

        if not user.is_authenticated:

            raise Exception("Authentication credentials were not provided")

        else:

            return ProductCategory.objects.all()

    def resolve_all_inventory(root, info):

        user = info.context.user

        if not user.is_authenticated:

            raise Exception("Authentication credentials were not provided")

        else:

            return ProductInventory.objects.all()