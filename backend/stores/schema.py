import graphene
from graphene_django.types import DjangoObjectType
from stores.models import Store, Room


class StoreType(DjangoObjectType):
    class Meta:
        model = Store


class RoomType(DjangoObjectType):
    class Meta:
        model = Room


class Query(graphene.ObjectType):
    stores = graphene.List(StoreType)
    rooms = graphene.List(RoomType)

    def resolve_stores(self, info):
        return Store.objects.all()

    def resolve_rooms(self, info):
        return Room.objects.all()


schema = graphene.Schema(query=Query)
