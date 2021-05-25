from django.contrib import admin
from .models import User_keys


class CustomUserAdmin(admin.ModelAdmin):
    model = User_keys
    list_display = ('username',)

admin.site.register(User_keys, CustomUserAdmin)
