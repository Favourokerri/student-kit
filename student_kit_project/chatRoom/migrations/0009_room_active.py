# Generated by Django 4.2.6 on 2023-11-03 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatRoom', '0008_room_members_remove_room_agora_token_delete_message_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
