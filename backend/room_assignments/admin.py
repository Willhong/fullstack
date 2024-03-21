from django.contrib import admin
from .models import RoomAssignment, RoomAssignmentHistory


@admin.register(RoomAssignment)
class RoomAssignmentAdmin(admin.ModelAdmin):
    list_display = ('idx', 'room', 'user', 'check_in_time',
                    'check_out_time', 'status')
    list_filter = ('room', 'user', 'status')
    search_fields = ('room', 'user', 'status')


@admin.register(RoomAssignmentHistory)
class RoomAssignmentHistoryAdmin(admin.ModelAdmin):
    list_display = ('idx', 'assignment', 'room', 'user',
                    'action', 'action_time', 'note')
    list_filter = ('room', 'user', 'action', 'action_time')
    search_fields = ('assignment', 'room', 'user', 'action', 'note')
