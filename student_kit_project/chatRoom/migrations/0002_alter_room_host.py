# Generated by Django 4.2.6 on 2023-10-29 23:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0008_alter_profile_profile_image'),
        ('chatRoom', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='host',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_profile.profile'),
        ),
    ]
