from django.contrib import admin
from .models import Product, Order, OrderHistory


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('idx', 'store', 'name', 'price', 'category')
    list_filter = ('store', 'category')
    search_fields = ('name', 'category')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('idx', 'room', 'product', 'quantity',
                    'status', 'created_at', 'served_at')
    list_filter = ('room', 'product', 'status')
    search_fields = ('room', 'product', 'status')


@admin.register(OrderHistory)
class OrderHistoryAdmin(admin.ModelAdmin):
    list_display = ('idx', 'order', 'store', 'action', 'action_time', 'note')
    list_filter = ('store', 'action')
    search_fields = ('order', 'store', 'action', 'note')
