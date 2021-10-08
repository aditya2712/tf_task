# Generated by Django 3.2.8 on 2021-10-08 17:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('discord', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discord_Guild',
            fields=[
                ('name', models.CharField(max_length=128)),
                ('guild_uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
    ]
