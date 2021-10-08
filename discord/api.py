from rest_framework import generics

from .serializers import DiscordGuildSerializer


class CreateDiscordGuild(generics.CreateAPIView):
    serializer_class = DiscordGuildSerializer
