from django.db import models

class Discord_User(models.Model):
    discord_uid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    guilds = models.ManyToManyField('Discord_Guild')

    def __str__(self):
        return str(self.discord_uid)+"-"+self.name


class Discord_Guild(models.Model):
    name = models.CharField(max_length=128)
    guild_uid = models.AutoField(primary_key=True)

    def __str__(self):
        return str(self.guild_uid)+"-"+self.name
