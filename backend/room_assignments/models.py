from django.db import models


class RoomAssignment(models.Model):
    idx = models.AutoField(primary_key=True)
    room = models.ForeignKey('stores.Room', on_delete=models.DO_NOTHING)
    user = models.ForeignKey('users.User', on_delete=models.DO_NOTHING)
    check_in_time = models.DateTimeField(auto_now_add=True)
    check_out_time = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20)

    def __str__(self):
        return f"Assignment {self.id} for {self.room.room_name}"


class RoomAssignmentHistory(models.Model):
    idx = models.AutoField(primary_key=True)
    assignment = models.ForeignKey(
        'RoomAssignment', on_delete=models.DO_NOTHING)
    room = models.ForeignKey('stores.Room', on_delete=models.DO_NOTHING)
    user = models.ForeignKey('users.User', on_delete=models.DO_NOTHING)
    action = models.CharField(max_length=20)
    action_time = models.DateTimeField(auto_now_add=True)
    note = models.TextField(null=True, blank=True)
