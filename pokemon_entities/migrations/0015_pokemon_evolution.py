# Generated by Django 3.1.14 on 2022-03-27 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0014_auto_20220325_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='evolution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pokemon_entities.pokemon'),
        ),
    ]