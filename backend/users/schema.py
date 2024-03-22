import graphene
from graphene_django.types import DjangoObjectType
from users.models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User


class Query(graphene.ObjectType):
    users = graphene.List(UserType)

    def resolve_users(self, info):
        return User.objects.all()


schema = graphene.Schema(query=Query)
