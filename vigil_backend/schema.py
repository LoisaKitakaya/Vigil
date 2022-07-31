import graphene
import users.schema as users_schema
import products.schema as products_schema
import orders.schema as orders_schema

# Graphene (code first) implementations. Soon to be discontinued

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
    products_schema.Mutation,
    orders_schema.Mutation,

    # graphene object type 
    graphene.ObjectType
    ):

    pass

# To resume with the graphene implementation

# uncomment the code below.

# schema = graphene.Schema(mutation=Mutation, query=Query)

# Ariadne (schema first) implementation. API backend

# Your schema here

