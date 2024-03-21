from django.contrib import admin
from .models import Store


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['name',  'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'location']
