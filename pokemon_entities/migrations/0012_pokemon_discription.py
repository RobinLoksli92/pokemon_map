# Generated by Django 3.1.14 on 2022-03-25 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0011_auto_20220324_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='discription',
            field=models.TextField(blank=True),
        ),
    ]
