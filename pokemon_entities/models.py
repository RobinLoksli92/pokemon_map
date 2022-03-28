from django.db import models
from django.forms import FloatField  # noqa F401
from django.conf import settings


class Pokemon(models.Model):
    title_ru = models.CharField(max_length=200, blank=True)
    title_en = models.CharField(max_length=200, blank=True)
    title_jp = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to=settings.MEDIA_ROOT, null=True, blank=True)
    appeared_at = models.DateTimeField(null=True, blank=True)
    disappeared_at = models.DateTimeField(null=True, blank=True)
    level = models.IntegerField(null=True, blank=True)
    health = models.IntegerField(null=True, blank=True)
    strength = models.IntegerField(null=True, blank=True)
    defence = models.IntegerField(null=True, blank=True)
    stamina = models.IntegerField(null=True, blank=True)
    discription = models.TextField(null=True, blank=True)
    evolution_from = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    # evolution_to = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.title_ru)


class PokemonEntity(models.Model):
    lat = models.FloatField(blank=True)
    long = models.FloatField(blank=True)
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, default='1')
    

    def __str__(self):
        return '{}'.format(self.pokemon)