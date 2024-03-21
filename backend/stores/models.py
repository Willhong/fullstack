from django.db import models

# Create your models here.


class Store(models.Model):
    idx = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    manager = models.ForeignKey(
        'users.User', on_delete=models.DO_NOTHING, null=True, blank=True, related_name='store_manager')
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Room(models.Model):
    idx = models.AutoField(primary_key=True)
    store = models.ForeignKey('Store', on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    is_open = models.BooleanField(default=True)
