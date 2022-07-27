import graphene
from graphene_django import DjangoObjectType
from .models import Product, ProductCategory, ProductInventory, ProductReview, ProductBrand

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

class ProductReviewObject(DjangoObjectType):

    class Meta:

        model = ProductReview

        fields = '__all__'

class ProductBrandObject(DjangoObjectType):

    class Meta:

        model = ProductBrand

        fields = '__all__'

class Query(graphene.ObjectType):

    all_products = graphene.List(ProductObject)

    home_products = graphene.List(ProductObject, limit=graphene.Int(required=True))

    single_product = graphene.Field(ProductObject, slug=graphene.String(required=True))
    single_category = graphene.List(ProductObject, slug=graphene.String(required=True))
    single_brand = graphene.List(ProductObject, slug=graphene.String(required=True))

    # resolving queries
    def resolve_all_products(root, info):

        return Product.objects.all()

    def resolve_home_products(root, info, limit):

        return Product.objects.all()[:limit]

    def resolve_single_product(root, info, slug):

        return Product.objects.get(slug=slug)

    def resolve_single_category(root, info, slug):

        return Product.objects.filter(product_category__slug=slug)

    def resolve_single_brand(root, info, slug):

        return Product.objects.filter(product_brand__slug=slug)