from django.db import migrations
from django.db import models


def delete_none_value(apps, schema_editor):
    Pokemon = apps.get_model('pokemon_entities', 'Pokemon')
    for pokemon in Pokemon.objects.all():
        pokemon.title = models.CharField(max_length=120, verbose_name='название на руссокм')
        pokemon.title_en = models.CharField(max_length=120, verbose_name='название на анлгийском')
        pokemon.title_jp = models.CharField(max_length=120, verbose_name='название на японском')


class Migration(migrations.Migration):
    dependencies = [
        ('pokemon_entities', '0013_auto_20201027_0711'),
    ]

    operations = [
        migrations.RunPython(delete_none_value)
    ]
