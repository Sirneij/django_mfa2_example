from django.contrib import admin
from mfa.models import User_Keys


@admin.register(User_Keys)
class User_KeysAdmin(admin.ModelAdmin):
    list_display = ('username', 'added_on', 'key_type', 'owned_by_enterprise',)
