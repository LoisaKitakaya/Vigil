import graphene
import graphql_jwt
from graphene_django import DjangoObjectType
from .models import User, Address

# Your schema here
class UserObject(DjangoObjectType):

    class Meta:

        model = User

        fields = '__all__'

class AddressObject(DjangoObjectType):

    class Meta:

        model = Address

        fields = '__all__'

class UserMutation(graphene.Mutation):

    class Arguments:

        username = graphene.String(required=True)
        email = graphene.String(required=True)
        firstname = graphene.String(required=True)
        secondname = graphene.String(required=True)
        password1 = graphene.String(required=True)
        password2 = graphene.String(required=True)

    user = graphene.Field(UserObject)

    @classmethod
    def mutate(
        cls, root, info, 
        username, 
        email, 
        firstname, 
        secondname, 
        password1, 
        password2
        ):

        if not User.objects.filter(email=email).exists():

            if password1 == password2:

                user = User.objects.create(
                    username=username, 
                    email=email, 
                    first_name=firstname, 
                    last_name=secondname
                    )

            else:

                raise Exception("Passwords provided did not match!")

            new_user = User.objects.get(email=email)

            new_user.set_password(password1)

            new_user.save()

        else:

            raise Exception("A user with the same email already exists. Make sure your email is unique!")

        return UserMutation(user=user)

class AddressMutation(graphene.Mutation):

    class Arguments:

        city = graphene.String(required=True)
        address = graphene.String(required=True)
        phone_one = graphene.String(required=True)
        phone_two = graphene.String(required=True)

    user_address = graphene.Field(AddressObject)

    @classmethod
    def mutate(
        cls, root, info,
        city,
        address,
        phone_one,
        phone_two
    ):

        user = info.context.user

        if not user.is_authenticated:

            raise Exception("Authentication credentials were not provided")

        else:

            user_address = Address.objects.create(
                user=user,
                city=city,
                address=address,
                phone_one=phone_one,
                phone_two=phone_two
            )

        return AddressMutation(user_address=user_address)

class Mutation(graphene.ObjectType):

    # jwt mutations
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    revoke_token = graphql_jwt.Revoke.Field()

    # custom mutations
    register_user = UserMutation.Field()
    add_address = AddressMutation.Field()

class Query(graphene.ObjectType):

    all_users = graphene.List(UserObject)

    def resolve_all_users(root, info):

        return User.objects.all()