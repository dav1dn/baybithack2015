from django.contrib import admin
from bithack.models import Hacker


class HackerAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'school', 'email']
    raw_id_fields = ['user']

admin.site.register(Hacker, HackerAdmin)
