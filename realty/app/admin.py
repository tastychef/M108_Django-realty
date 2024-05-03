from django.contrib import admin
from .models import Zhk


@admin.register(Zhk)
class AppAdmin(admin.ModelAdmin):
    list_display = ('name_project', 'name_developer')
