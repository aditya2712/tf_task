from django.db import models
from django.db.models import fields
from rest_framework import serializers

from .models import Discord_Guild, Discord_User

class DiscordGuildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discord_Guild
        fields = '__all__'
