from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexPortada, name='indexPortada'),
    path('peliculas/<int:pelicula_id>/', views.show_pelicula, name='show_pelicula'),
    path('generos/<int:genero_id>/peliculas', views.peliculasGenero, name='peliculasGenero'),
    path('directores/<int:director_id>/peliculas', views.peliculasDirector, name='peliculasDirector'),
    path('directores/<int:director_id>', views.show_director, name='show_director'),
    path('generos/<int:genero_id>', views.show_genero, name='show_genero'),
    path("peliculas/", views.index_peliculas, name="index_peliculas"),
    path("generos/", views.index_generos, name="index_generos"),
    path("directores/", views.index_directores, name="index_directores"),
]