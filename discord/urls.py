from django.urls import path, re_path

from .api import CreateDiscordGuild, CommonMembersPercentage


urlpatterns = [
    path('discord_guild/create', CreateDiscordGuild.as_view(), name='create-discord-guild'),
    path('discord_match_percentage/', CommonMembersPercentage, name='percentage-of-common-members')
]
