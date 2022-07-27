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

class ProductReviewMutation(graphene.Mutation):

    class Arguments:

        item_name = graphene.String(required=True)
        item_rating = graphene.Int(required=True)
        item_review = graphene.String(required=True)

    review = graphene.Field(ProductReviewObject)

    @classmethod
    def mutate(
        cls, root, info,
        item_name,
        item_rating,
        item_review
    ):

        user = info.context.user

        if not user.is_authenticated:

            raise Exception("Authentication credentials were not provided")

        product = Product.objects.get(name=item_name)

        review = ProductReview.objects.create(
            user=user,
            name=item_name,
            rating=item_rating,
            review=item_review
        )

        product.product_review.add(review)

        return ProductReviewMutation(review=review)

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

class Mutation(graphene.ObjectType):

    add_review = ProductReviewMutation.Field()