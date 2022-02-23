from distutils.command.upload import upload
from pyexpat import model
from statistics import mode
from django.db import models
from django.forms import FloatField  # noqa F401

# your models here
class Pokemon(models.Model):
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.title)


class PokemonEntity(models.Model):
    longitude = models.FloatField(blank=True)
    latitude = models.FloatField(blank=True)
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, default='1')