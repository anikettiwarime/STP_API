from django.apps import AppConfig
from django.db.models import UUIDField, AutoField


class CustomUUIDField(UUIDField, AutoField):
    pass


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'auth_users'
