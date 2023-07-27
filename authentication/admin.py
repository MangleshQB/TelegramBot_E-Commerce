from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(CustomUser)
class UserAccountAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'username', 'is_active']
    list_editable = ['is_active']
    search_fields = ['username', 'id', 'email']



