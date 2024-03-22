import graphene
from graphene_django.types import DjangoObjectType
from room_assignments.models import RoomAssignment, RoomAssignmentHistory


class RoomAssignmentType(DjangoObjectType):
    class Meta:
        model = RoomAssignment


class RoomAssignmentHistoryType(DjangoObjectType):
    class Meta:
        model = RoomAssignmentHistory


class Query(graphene.ObjectType):
    room_assignments = graphene.List(RoomAssignmentType)
    room_assignment_histories = graphene.List(RoomAssignmentHistoryType)

    def resolve_room_assignments(self, info):
        return RoomAssignment.objects.all()

    def resolve_room_assignment_histories(self, info):
        return RoomAssignmentHistory.objects.all()


schema = graphene.Schema(query=Query)
