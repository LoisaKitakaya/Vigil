import graphene
import graphql_jwt
from graphene_django import DjangoObjectType
from .models import User, UserAddress

# Your schema here
class UserObject(DjangoObjectType):

    class Meta:

        model = User

        fields = '__all__'

class UserAddressObject(DjangoObjectType):

    class Meta:

        model = UserAddress

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
    def mutate(cls, root, info, username, email, firstname, secondname, password1, password2):

        if not User.objects.filter(email=email).exists():

            if password1 == password2:

                user = User.objects.create(username=username, email=email, first_name=firstname, last_name=secondname)

            else:

                raise Exception("Passwords provided did not match!")

            new_user = User.objects.get(email=email)

            new_user.set_password(password1)

            new_user.save()

        else:

            raise Exception("A user with the same email already exists. Make sure your email is unique!")

        return UserMutation(user=user)

class Mutation(graphene.ObjectType):

    # jwt mutations
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    revoke_token = graphql_jwt.Revoke.Field()

    # custom mutations
    register_user = UserMutation.Field()

class Query(graphene.ObjectType):

    all_users = graphene.List(UserObject)

    def resolve_all_users(root, info):

        print(info.context.user)

        return User.objects.all()