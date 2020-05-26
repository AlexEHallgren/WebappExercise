from django.test import TestCase
from django.urls import reverse
from django.http import HttpResponseServerError

import requests
import responses
from responses import GET
import ghibli.views
from app.config import app_config

class FilmListViewTest(TestCase):
    films_url = app_config.ghibli.films_url
    people_url = app_config.ghibli.people_url
    # Correct data from the films endpoint
    film_data = [
        {
            'id': 'f1',
            'title': 'Great Film',
            'director': 'Awesome Director',
            'people': [],
            'url': 'films/url'
        }
    ]
    # Correct data from the people endpoint
    actor_data = [
        {
            'id': 'a1',
            'name': 'Person One',
            'films': [
                'https://ghibliapi.herokuapp.com/films/f1'
            ]
        },
        {
            'id': 'a2',
            'name': 'Person Two',
            'films': []
        }
    ] 
    # Correct matching of films & people
    films_with_people = [
        {
            'title': 'Great Film',
            'people': [
                {
                    'name': 'Person One'
                }
            ]
        }
    ]
    
    @responses.activate
    def test_view_url_exists(self):
        responses.add(GET, self.films_url, json=self.film_data, status=200)
        responses.add(GET, self.people_url, json=self.actor_data, status=200)
        self.assertEquals(self.client.get('/movies/').status_code, 200)
    
    @responses.activate
    def test_view_url_accessible_by_name(self):
        responses.add(GET, self.films_url, json=self.film_data, status=200)
        responses.add(GET, self.people_url, json=self.actor_data, status=200)
        resp = self.client.get(reverse('ghibli:movies'))
        self.assertEqual(resp.status_code, 200)

    @responses.activate 
    def test_view_uses_correct_template(self):
        responses.add(GET, self.films_url, json=self.film_data, status=200)
        responses.add(GET, self.people_url, json=self.actor_data, status=200)
        resp = self.client.get(reverse('ghibli:movies'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'ghibli/film_list.html')

    @responses.activate
    def test_view_returns_correct_data(self):
        responses.add(GET, self.films_url, json=self.film_data, status=200)
        responses.add(GET, self.people_url, json=self.actor_data, status=200)
        resp = self.client.get(reverse('ghibli:movies'))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context['film_list'], self.films_with_people)

    @responses.activate
    def test_view_returns_500_on_timeout(self):
        responses.add(GET, self.films_url, body=requests.Timeout())
        resp = self.client.get(reverse('ghibli:movies'))
        self.assertEqual(resp.status_code, 500)

    @responses.activate
    def test_view_uses_cache(self):
        """ Mock different response for the second GET to verify it isn't called twice """
        responses.add(GET, self.films_url, json=self.film_data, status=200)
        responses.add(GET, self.people_url, json=self.actor_data, status=200)
        responses.add(GET, self.films_url, json='', status=200)
        responses.add(GET, self.people_url, json='', status=200)
        resp = self.client.get(reverse('ghibli:movies'))
        self.assertFalse(resp.context['film_list'] == '')



