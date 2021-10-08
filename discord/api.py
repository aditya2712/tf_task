from django.http.response import HttpResponse
from rest_framework import generics

from .serializers import DiscordGuildSerializer
from .models import Discord_Guild

class CreateDiscordGuild(generics.CreateAPIView):
    serializer_class = DiscordGuildSerializer

def CommonMembersPercentage(request):
    arr = request.GET['guild_uid1'].split(',')
    guild_id1 = arr[0]
    guild_id2 = arr[1].split('=')[1]
    try:
        guild1 = Discord_Guild.objects.get(guild_uid=guild_id1)
        guild2 = Discord_Guild.objects.get(guild_uid=guild_id2)
        guild1_user_cnt = len(guild1.discord_user_set.all());
        common_count = len(guild1.discord_user_set.all() & guild2.discord_user_set.all())
        return HttpResponse(str((common_count/guild1_user_cnt)*100)+"%")
    except:
        return HttpResponse("something went wrong")
