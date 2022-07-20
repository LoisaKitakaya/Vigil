import graphene
import users.schema as users_schema

# Your schema here
class Query(
    # custom Queries
    users_schema.Query,

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