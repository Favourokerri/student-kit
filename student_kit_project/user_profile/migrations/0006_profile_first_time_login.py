# Generated by Django 4.2.6 on 2023-10-22 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0005_alter_profile_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='first_time_login',
            field=models.BooleanField(default=True),
        ),
    ]
