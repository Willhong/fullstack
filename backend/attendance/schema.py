import graphene
from graphene_django.types import DjangoObjectType
from attendance.models import Attendance, AttendanceHistory


class AttendanceType(DjangoObjectType):
    class Meta:
        model = Attendance


class AttendanceHistoryType(DjangoObjectType):
    class Meta:
        model = AttendanceHistory


class Query(graphene.ObjectType):
    attendances = graphene.List(AttendanceType)
    attendance_histories = graphene.List(AttendanceHistoryType)

    def resolve_attendances(self, info):
        return Attendance.objects.all()

    def resolve_attendance_histories(self, info):
        return AttendanceHistory.objects.all()


schema = graphene.Schema(query=Query)
