# Generated by Django 3.1.14 on 2022-03-29 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0020_auto_20220328_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='discription',
            field=models.TextField(blank=True, default='Описание в разработке', verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title_en',
            field=models.CharField(blank=True, default=' ', max_length=50, verbose_name='Название покемона англ.'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title_jp',
            field=models.CharField(blank=True, default=' ', max_length=50, verbose_name='Название покемона яп.'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title_ru',
            field=models.CharField(max_length=50, verbose_name='Название покемона рус.'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='lat',
            field=models.FloatField(verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='long',
            field=models.FloatField(verbose_name='Долгота'),
        ),
    ]
