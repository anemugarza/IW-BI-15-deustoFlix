from django.shortcuts import render, get_object_or_404, get_list_or_404, HttpResponseRedirect
from django.http import HttpResponse
from .models import Genero, Pelicula, Director
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
import json

from django.utils.translation import gettext as _
from django.utils.translation import get_language,activate, gettext


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
from django.shortcuts import render
from django.utils.translation import gettext as _, activate, get_language
from .models import Genero, Pelicula


def indexPortada(request):
    peliculasMasVistas = []

    for genero in Genero.objects.all():
        pelicula_mas_vista = Pelicula.objects.filter(genero=genero).order_by('-vecesVista').first()
        if pelicula_mas_vista:
            peliculasMasVistas.append(pelicula_mas_vista)

    curl_language = get_language()
    try:
        activate('eu')  
        trans_text = _("Películas más vistas de cada género")
    finally:
        activate(curl_language)

    context = {"lista_peliculasMasVistas": peliculasMasVistas, "trans_text": trans_text}
    
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