from django.contrib import admin
from models import SqrlClient


class SqrlClientAdmin(admin.ModelAdmin):
    list_display = ('vuk', 'user')

admin.site.register(SqrlClient, SqrlClientAdmin)
