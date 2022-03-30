# Generated by Django 3.1.14 on 2022-02-23 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0005_pokemonentity_pokemon'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='appeared_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='disappeared_at',
            field=models.DateTimeField(null=True),
        ),
    ]