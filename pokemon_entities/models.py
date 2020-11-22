from django.db import models


class Pokemon(models.Model):
    title = models.CharField(max_length=120, verbose_name='название на руссокм')
    title_en = models.CharField(max_length=120, verbose_name='название на анлгийском')
    title_jp = models.CharField(max_length=120, verbose_name='название на японском')
    image = models.ImageField(null=True, blank=True, verbose_name='картинка')
    description = models.TextField(verbose_name='Описание')
    previous_evolution = models.ForeignKey('self',
                                           on_delete=models.SET_NULL,
                                           blank=True,
                                           null=True,
                                           related_name='next_evolutions',
                                           verbose_name='предыдущая эволюция')

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    lat = models.FloatField(null=True, verbose_name='широта')
    lon = models.FloatField(null=True, verbose_name='долгота')
    appeared_at = models.DateTimeField(verbose_name='время появления')
    disappeared_at = models.DateTimeField(verbose_name='времяс исчезновения')
    level = models.IntegerField(null=True, verbose_name='уровень')
    health = models.IntegerField(null=True, verbose_name='здоровье')
    strength = models.IntegerField(null=True, verbose_name='сила')
    defence = models.IntegerField(null=True, verbose_name='защита')
    stamina = models.IntegerField(null=True, verbose_name='мана')
    pokemon = models.ForeignKey(Pokemon, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='покемон')
