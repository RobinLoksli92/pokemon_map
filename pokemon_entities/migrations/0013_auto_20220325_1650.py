# Generated by Django 3.1.14 on 2022-03-25 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0012_pokemon_discription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='discription',
            field=models.TextField(),
        ),
    ]
