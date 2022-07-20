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

