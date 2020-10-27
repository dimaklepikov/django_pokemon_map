# Django_pokemon_map

![screenshot](https://dvmn.org/filer/canonical/1563275070/172/)

### Scope of usage:

Web-site about [Pokemon GO](https://www.pokemongo.com/en-us/) game. This is about catching [pokemons](https://ru.wikipedia.org/wiki/%D0%9F%D0%BE%D0%BA%D0%B5%D0%BC%D0%BE%D0%BD).

Pokemons appears on map at some period of time. Every player can catch Pokemon to his own collection.

You can find differend entities od one Pokemon: for example, 3 entities of Bulbasaur. Any playeer can collect the same individual of pokemon. When player take his Pokemon, it's disappered for him but not for other players.

Also there are an evolution mechanic. One type Pokemon can evolve to another one. Bulbasaur evaluates to Ivisaur, and Ivisaur turns to Venusaur.


### How to run

You need Python 3+

Fork or download this repository, set up requirements
```sh
pip install -r requirements.txt
```

run Django local host

```sh
python3 manage.py runserver
```

### Environment variables

You need to set up `.env` on the same level with `manage.py` and set variables like: `VARIABLE=value`.

Avaliable variables:
- `DEBUG` — debug-mode. Set 'True' if you want to test sth
- `SECRET_KEY` — secret key of project

## Goals of project:

To have fun and get more understanding about beautiful world of [Django](https://www.djangoproject.com/)

