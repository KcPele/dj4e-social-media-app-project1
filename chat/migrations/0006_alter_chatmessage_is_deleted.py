# Generated by Django 3.2.9 on 2021-11-28 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_alter_chatmessage_reciever'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmessage',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
