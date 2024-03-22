# schema.py
import graphene
from graphene_django.types import DjangoObjectType
import users.schema
import stores.schema
import room_assignments.schema
import orders.schema
import attendance.schema


class Query(users.schema.Query,
            stores.schema.Query,
            room_assignments.schema.Query,
            orders.schema.Query,
            attendance.schema.Query,
            graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
