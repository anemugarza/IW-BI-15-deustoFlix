from django.shortcuts import render, get_object_or_404, get_list_or_404, HttpResponseRedirect
from django.http import HttpResponse
from .models import Genero, Pelicula, Director
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
import json


#devuelve el listado de generos
class IndexGeneros(ListView):
	model = Genero
	template_name = 'generos.html'
	queryset = Genero.objects.order_by('nombre')



#devuelve los datos de un genero
class ShowGenero(DetailView):
	model = Genero
	template_name = 'genero.html'
	def get_context_data(self, **kwargs):
			context = super().get_context_data(**kwargs)
			genero = self.get_object()
			context['peliculasGenero'] = genero.pelicula_set.all()
			return context


#devuelve el listado de peliculas
class IndexPeliculas(ListView):
	model = Pelicula
	queryset = Pelicula.objects.order_by('nombre')
	template_name = 'peliculas.html'



#devuelve los datos de una pelicula
class ShowPelicula(DetailView):
	model = Pelicula		
	template_name = 'pelicula.html'
	
#devuelve el listado de directores
class IndexDirectores(ListView):
	model = Director
	queryset = Director.objects.order_by('-nombre')
	template_name = 'directores.html'



#devuelve los datos de un director
class ShowDirector(DetailView):
	model = Director
	template_name = 'director.html'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		director = self.get_object()
		context['peliculasDirector'] = director.pelicula_set.all()
		return context


#Devuelve la pelicula mas vista de cada genero
def indexPortada(request):
	peliculasMasVistas = []  # Una lista de objetos de modelo Pelicula

	for genero in Genero.objects.all():
		pelicula_mas_vista = Pelicula.objects.filter(genero=genero).order_by('-vecesVista').first()
		if pelicula_mas_vista:
			peliculasMasVistas.append(pelicula_mas_vista)
	context = {"lista_peliculasMasVistas": peliculasMasVistas}
	return render(request, "index.html", context)

