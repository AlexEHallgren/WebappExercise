from django.shortcuts import render, redirect
from django.core.cache import caches
from django.http import HttpResponseServerError
from requests import RequestException

from .models import Film, Person
from .utility import HttpWrapper
from app.config import app_config

_cache = caches['ghibli']
_film_cache_key = app_config.ghibli.film_data_cache_key
_http_client = HttpWrapper('ghibli_view')

def match_films_with_actors(films, actors):
    films_by_id = { f['id']:Film(f['title'], f['id']) for f in films }
    for actor in actors:
        for film_url in actor['films']:
            film_id = film_url.split('/')[-1]
            films_by_id[film_id].add_person_by_name(actor['name'])
    json_list = [f.as_json() for f in films_by_id.values()]
    return json_list

def film_list_view(request):
    cached_list = _cache.get(_film_cache_key)
    if cached_list:
        film_list = cached_list
    else:    
        try:
            films_resp = _http_client.get_url(app_config.ghibli.films_url).json()
            actors_resp = _http_client.get_url(app_config.ghibli.people_url).json()
            film_list = match_films_with_actors(films_resp, actors_resp)
            _cache.set(app_config.ghibli.film_data_cache_key, film_list, 60)
        except RequestException:
            return HttpResponseServerError("Something went wrong!")
    
    context = {
        'film_list': film_list,
    }
    return render(request, 'ghibli/film_list.html', context)
