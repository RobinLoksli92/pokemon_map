from django.db import models
from django.forms import FloatField  # noqa F401
from django.conf import settings


class Pokemon(models.Model):
    title_ru = models.CharField('Название покемона рус.', max_length=50)
    title_en = models.CharField('Название покемона англ.',max_length=50, blank=True)
    title_jp = models.CharField('Название покемона яп.',max_length=50, blank=True)
    image = models.ImageField('Картинка покемона',upload_to=settings.MEDIA_ROOT)
    discription = models.TextField('Описание',blank=True)
    evolution_from = models.ForeignKey('self', verbose_name='Эволюционировал из', on_delete=models.CASCADE, null=True, blank=True, related_name='evolution_to')

    def __str__(self):
        return self.title_ru


class PokemonEntity(models.Model):
    lat = models.FloatField('Широта')
    long = models.FloatField('Долгота')
    pokemon = models.ForeignKey(Pokemon, verbose_name='Покемон', on_delete=models.CASCADE)
    appeared_at = models.DateTimeField('Появится в')
    disappeared_at = models.DateTimeField('Исчезнет в')
    level = models.IntegerField('Уровень')
    health = models.IntegerField('Здоровье')
    strength = models.IntegerField('Сила')
    defence = models.IntegerField('Защита')
    stamina = models.IntegerField('Выносливость')

    def __str__(self):
        return '{}'.format(self.pokemon)