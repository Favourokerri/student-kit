# Generated by Django 4.2.6 on 2023-11-12 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0006_rename_card_items_card_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card_item',
            name='question',
            field=models.TextField(max_length=200),
        ),
    ]
