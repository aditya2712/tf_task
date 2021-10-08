from django.contrib import admin

from .models import Discord_User, Discord_Guild

admin.site.register(Discord_User)
admin.site.register(Discord_Guild)
