# Generated by Django 3.2.9 on 2021-11-20 15:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20211120_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]