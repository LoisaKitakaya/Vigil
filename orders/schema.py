import graphene
from graphene_django import DjangoObjectType
from .models import CartItem, Order

class CartItemObject(DjangoObjectType):

    class Meta:

        model = CartItem

        fields = '__all__'

class Order(DjangoObjectType):

    class Meta:

        model = Order

        fields = '__all__'