from django.contrib import admin

# Register your models here.

from .models import Player

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'skill_level')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('skill_level',)
