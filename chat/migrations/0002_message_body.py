# Generated by Django 3.2.9 on 2021-11-27 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='body',
            field=models.CharField(default='', max_length=370),
        ),
    ]
