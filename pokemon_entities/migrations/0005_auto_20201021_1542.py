# Generated by Django 2.2.3 on 2020-10-21 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0004_auto_20201021_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]