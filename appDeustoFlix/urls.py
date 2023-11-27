from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexPortada, name='indexPortada'),
    path('peliculas/<int:pk>/', views.ShowPelicula.as_view(), name='ShowPelicula'),
    path('directores/<int:director_id>/', views.ShowDirector.as_view(), name='ShowDirector'),
    path('generos/<int:genero_id>/', views.ShowGenero.as_view(), name='ShowGenero'),
    path("peliculas/", views.IndexPeliculas.as_view(), name="IndexPeliculas"),
    path("generos/", views.IndexGeneros.as_view(), name="IndexGeneros"),
    path("directores/", views.IndexDirectores.as_view(), name="IndexDirectores"),
]