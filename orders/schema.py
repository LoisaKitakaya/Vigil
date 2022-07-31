import graphene
from graphene_django import DjangoObjectType
from .models import CartItem, DeliveryOrder, PickupOrder
import string 
import random 

class CartItemObject(DjangoObjectType):

    class Meta:

        model = CartItem

        fields = '__all__'

class DeliveryOrderObject(DjangoObjectType):

    class Meta:

        model = DeliveryOrder

        fields = '__all__'

class PickupOrderObject(DjangoObjectType):

    class Meta:

        model = PickupOrder

        fields = '__all__'

class CartItemInput(graphene.InputObjectType):

    name = graphene.String(required=True)
    price = graphene.Float(required=True)
    thumbnail = graphene.String(required=True)
    quantity = graphene.Int(required=True)

class DeliveryMutation(graphene.Mutation):

    class Arguments:

        city = graphene.String(required=True)
        address = graphene.String(required=True)
        phone = graphene.String(required=True)
        items = graphene.List(CartItemInput, required=True)
        total = graphene.Float(required=True)

    order = graphene.Field(DeliveryOrderObject)

    @classmethod
    def mutate(
        cls, root, info,
        city,
        address,
        phone,
        items,
        total
    ):

        user = info.context.user

        if not user.is_authenticated:

            raise Exception("Authentication credentials were not provided")

        else:

            N = 10

            res = ''.join(random.choices(string.ascii_uppercase +  string.digits, k = N))

            order = DeliveryOrder.objects.create(
                user=user,
                city=city,
                address=address,
                phone=phone,
                order_uic=res,
                total=total,
            )

            for item in items:

                cart_item = CartItem(
                    name=item.name,
                    price=item.price,
                    thumbnail=item.thumbnail,
                    quantity=item.quantity
                )

                cart_item.save()

                order.item.add(cart_item)

            print(items)

            return DeliveryMutation(order=order)

class Mutation(graphene.ObjectType):

    create_order = DeliveryMutation.Field()