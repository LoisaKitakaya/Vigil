import graphene
import users.schema as users_schema
import products.schema as products_schema

# Your schema here
class Query(
    # custom Queries
    products_schema.Query,

    # graphene object type
    graphene.ObjectType
    ):

    pass

class Mutation(
    # custom Queries
    users_schema.Mutation,

    # graphene object type 
    graphene.ObjectType
    ):

    pass

schema = graphene.Schema(mutation=Mutation, query=Query)