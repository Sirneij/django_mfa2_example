from django.contrib import admin
from mfa.models import User_Keys


class CustomUserAdmin(admin.ModelAdmin):
    model = User_Keys
    list_display = ('username',)

admin.site.register(User_Keys, CustomUserAdmin)
