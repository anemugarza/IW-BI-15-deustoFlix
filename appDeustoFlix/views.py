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
	queryset = Genero.objects.all()

#devuelve los datos de un genero
class ShowGenero(DetailView):
	def show_genero(request, genero_id):
		genero = get_object_or_404(Genero, pk=genero_id)
		peliculasGenero = genero.pelicula_set.all()
		context = {'genero': genero ,'peliculasGenero' : peliculasGenero }	
		return render(request, 'genero.html', context)


#devuelve el listado de peliculas
class IndexPeliculas(ListView):
	model = Pelicula
	queryset = Pelicula.objects.all()

#devuelve los datos de una pelicula
class ShowPelicula(DetailView):
	def show_pelicula(request, pelicula_id):
		pelicula = get_object_or_404(Pelicula, pk=pelicula_id)
		context = {'pelicula': pelicula }
		return render(request, 'pelicula.html', context)

#devuelve el listado de directores
class IndexDirectores(ListView):
	model = Director
	queryset = Director.objects.all()

#devuelve los datos de un director
class ShowDirector(DetailView):
	def show_director(request, director_id):
		director = get_object_or_404(Director, pk=director_id)
		peliculasDirector = director.pelicula_set.all()
		context = {'director': director , 'peliculasDirector':peliculasDirector}
		return render(request, 'director.html', context)


#Devuelve la pelicula mas vista de cada genero
class IndexPortada(View):
	def indexPortada(request):
		generos = Genero.objects.all()
		peliculasMasVistas = []  # Una lista de objetos de modelo Pelicula

		for genero in generos:
			pelicula_mas_vista = Pelicula.objects.filter(genero=genero).order_by('-vecesVista').first()
			if pelicula_mas_vista:
				peliculasMasVistas.append(pelicula_mas_vista)
		context = {"lista_peliculasMasVistas": peliculasMasVistas}
		return render(request, "index.html", context)




class Contacto(View):
    def get(self, request):
        context = {}
        return render(request, "contacto.html", context)
    
    def post(self, request):
        # Añade el mensaje enviado (con sus metadatos) al registro
        with open("mensajes.json", "a", encoding = "utf-8") as f:
            json.dump(request.POST, f, indent = 4)
        return HttpResponseRedirect("/") # Redirige a la página de inicio