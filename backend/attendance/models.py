from django.db import models


class Attendance(models.Model):
    idx = models.AutoField(primary_key=True)
    user = models.ForeignKey('users.User', on_delete=models.DO_NOTHING)
    store = models.ForeignKey('stores.Store', on_delete=models.DO_NOTHING)
    check_in_time = models.DateTimeField(auto_now_add=True)
    check_out_time = models.DateTimeField(null=True, blank=True)


class AttendanceHistory(models.Model):
    idx = models.AutoField(primary_key=True)
    user = models.ForeignKey('users.User', on_delete=models.DO_NOTHING)
    store = models.ForeignKey('stores.Store', on_delete=models.DO_NOTHING)
    action = models.CharField(max_length=20)
    action_time = models.DateTimeField(auto_now_add=True)
    note = models.TextField(null=True, blank=True)
