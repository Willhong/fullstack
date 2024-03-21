from django.contrib import admin
from .models import Attendance, AttendanceHistory


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('idx', 'user', 'store', 'check_in_time', 'check_out_time')
    list_filter = ('store', 'check_in_time', 'check_out_time')
    search_fields = ('user', 'store')


@admin.register(AttendanceHistory)
class AttendanceHistoryAdmin(admin.ModelAdmin):
    list_display = ('idx', 'user', 'store', 'action', 'action_time', 'note')
    list_filter = ('store', 'action', 'action_time')
    search_fields = ('user', 'store', 'action', 'note')
