# Generated by Django 3.1.14 on 2022-02-23 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0006_auto_20220223_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='defence',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='health',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='level',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='stamina',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='strength',
            field=models.IntegerField(null=True),
        ),
    ]
