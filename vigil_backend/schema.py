import graphene

# Your schema here
class Query(graphene.ObjectType):

    pass

class Mutation(graphene.ObjectType):

    pass

schema = graphene.Schema(mutation=Mutation, query=Query)