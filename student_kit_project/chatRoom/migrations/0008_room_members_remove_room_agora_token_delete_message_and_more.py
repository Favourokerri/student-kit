# Generated by Django 4.2.6 on 2023-11-03 09:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chatRoom', '0007_rename_stream_token_room_agora_token'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room_Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='room',
            name='agora_token',
        ),
        migrations.DeleteModel(
            name='message',
        ),
        migrations.AddField(
            model_name='room_members',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chatRoom.room'),
        ),
        migrations.AddField(
            model_name='room_members',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
