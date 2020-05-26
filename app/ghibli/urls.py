from django.urls import path

from . import views

app_name = 'ghibli'

urlpatterns = [
    path('', views.film_list_view, name='movies')
]