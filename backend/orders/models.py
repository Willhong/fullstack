from django.db import models


class Product(models.Model):
    idx = models.AutoField(primary_key=True)
    store = models.ForeignKey('stores.Store', on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Order(models.Model):
    idx = models.AutoField(primary_key=True)
    room = models.ForeignKey('stores.Room', on_delete=models.DO_NOTHING)
    product = models.ForeignKey('Product', on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    served_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Order {self.id} for {self.product.name}"


class OrderHistory(models.Model):
    idx = models.AutoField(primary_key=True)
    order = models.ForeignKey('Order', on_delete=models.DO_NOTHING)
    store = models.ForeignKey('stores.Store', on_delete=models.DO_NOTHING)
    action = models.CharField(max_length=20)
    action_time = models.DateTimeField(auto_now_add=True)
    note = models.TextField(null=True, blank=True)
