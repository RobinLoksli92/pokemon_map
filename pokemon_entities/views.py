import folium
import json

from django.http import HttpResponseNotFound
from django.shortcuts import render

from pokemon_entities.models import Pokemon, PokemonEntity


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    pokemons = Pokemon.objects.all()

    for pokemon in pokemons:
        pokemon_entity = PokemonEntity.objects.get(pokemon=pokemon)
        
        if pokemon.image:
            add_pokemon(
                folium_map, pokemon_entity.lat,
                pokemon_entity.long, request.build_absolute_uri(pokemon.image.url)
            )
        else:
            add_pokemon(
                folium_map, pokemon_entity.lat,
                pokemon_entity.long,
            )
    pokemons_on_page = []

    for pokemon in pokemons:
        if pokemon.image:
            pokemons_on_page.append({
                'pokemon_id':pokemon.id,
                'img_url': request.build_absolute_uri(pokemon.image.url),
                'title_ru': pokemon.title_ru
            })
        else:
            pokemons_on_page.append({
                'pokemon_id':pokemon.id,
                'title_ru': pokemon.title_ru
            }) 
    

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    requested_pokemon = Pokemon.objects.get(id = pokemon_id)
    pokemon_entity = PokemonEntity.objects.get(pokemon=requested_pokemon)
    
    pokemon = {
        'img_url': request.build_absolute_uri(requested_pokemon.image.url),
        'title_ru': requested_pokemon.title_ru,
        'title_en': requested_pokemon.title_en,
        'title_jp': requested_pokemon.title_jp,
        'description': requested_pokemon.discription,
        'lat': pokemon_entity.lat, 
        'long': pokemon_entity.long,
        
    }
    
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    
    add_pokemon(
        folium_map, pokemon['lat'],
        pokemon['long'], pokemon['img_url']
    )

    next_evolutions = requested_pokemon.evolution_to.all()
    if next_evolutions:
        pokemon['next_evolution'] = {
            'title_ru': next_evolutions[0].title_ru,
            'pokemon_id': next_evolutions[0].id,
            'img_url': request.build_absolute_uri(next_evolutions[0].image.url)
            }

    if requested_pokemon.evolution_from:
        pokemon['previous_evolution'] = {
            'title_ru': requested_pokemon.evolution_from,
            'pokemon_id': requested_pokemon.evolution_from.id ,
            'img_url': request.build_absolute_uri(requested_pokemon.evolution_from.image.url)
            }
        return render(request, 'pokemon.html', context={
            'map': folium_map._repr_html_(), 'pokemon': pokemon
        })
    else:
        return render(request, 'pokemon.html', context={
            'map': folium_map._repr_html_(), 'pokemon': pokemon
        })