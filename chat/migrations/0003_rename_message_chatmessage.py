# Generated by Django 3.2.9 on 2021-11-27 17:52

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0002_message_body'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Message',
            new_name='ChatMessage',
        ),
    ]