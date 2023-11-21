from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexPortada.as_view(), name='indexPortada'),
    path('peliculas/<int:pelicula_id>/', views.ShowPelicula.as_view(), name='show_pelicula'),
    path('directores/<int:director_id>', views.ShowDirector.as_view(), name='show_director'),
    path('generos/<int:genero_id>', views.ShowGenero.as_view(), name='show_genero'),
    path("peliculas/", views.IndexPeliculas.as_view(), name="index_peliculas"),
    path("generos/", views.IndexGeneros.as_view(), name="index_generos"),
    path("directores/", views.IndexDirectores.as_view(), name="index_directores"),
]