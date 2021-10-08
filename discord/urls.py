from django.urls import path

from .api import CreateDiscordGuild


urlpatterns = [
    path('discord_guild/create', CreateDiscordGuild.as_view(), name='create-discord-guild'),
]
