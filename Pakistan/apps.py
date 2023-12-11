from django.apps import AppConfig
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

admin.site.register(User, UserAdmin)

class PakistanConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Pakistan'
