# Generated by Django 4.2.6 on 2023-10-22 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Welcome_Notifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
