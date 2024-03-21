from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.dispatch import receiver


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        from .models import create_default_groups
        post_migrate.connect(create_default_groups, sender=self)
