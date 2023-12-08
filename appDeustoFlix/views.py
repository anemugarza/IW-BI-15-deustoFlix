from django.shortcuts import render, get_object_or_404, get_list_or_404, HttpResponseRedirect
from django.http import HttpResponse
from .models import Calificacion, Genero, Pelicula, Director
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
import json
from .forms import TuFormularioDeCalificacion
from django.utils.translation import gettext as _

#devuelve el listado de generos
class IndexGeneros(ListView):#bien
	model = Genero
	template_name = 'generos.html'
	queryset = Genero.objects.order_by('nombre')
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['hola'] = _('Hola')
		return context


#devuelve los datos de un genero
class ShowGenero(DetailView): #bien
	model = Genero
	template_name = 'genero.html'
	def get_context_data(self, **kwargs):
			context = super().get_context_data(**kwargs)
			genero = self.get_object()
			context['peliculasGenero'] = genero.pelicula_set.all()
			return context


#devuelve el listado de peliculas
class IndexPeliculas(ListView): #bien
	model = Pelicula
	queryset = Pelicula.objects.order_by('nombre')
	template_name = 'peliculas.html'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['hola'] = _('Hola')
		return context


#devuelve los datos de una pelicula
class ShowPelicula(DetailView): #bien
	model = Pelicula		
	template_name = 'pelicula.html'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['hola'] = _('Hola')
		return context

	
#devuelve el listado de directores
class IndexDirectores(ListView): #no
	model = Director
	queryset = Director.objects.order_by('-nombre')
	template_name = 'directores.html'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['hola'] = _('Hola')
		return context


#devuelve los datos de un director
class ShowDirector(DetailView): #no
	model = Director
	template_name = 'director.html'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		director = self.get_object()
		context['peliculasDirector'] = director.pelicula_set.all()
		return context


#Devuelve la pelicula mas vista de cada genero
def indexPortada(request): #bien
	peliculasMasVistas = []  # Una lista de objetos de modelo Pelicula

	for genero in Genero.objects.all():
		pelicula_mas_vista = Pelicula.objects.filter(genero=genero).order_by('-vecesVista').first()
		if pelicula_mas_vista:
			peliculasMasVistas.append(pelicula_mas_vista)
	context = {"lista_peliculasMasVistas": peliculasMasVistas,
				'hola': _('Hola')}
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
	



class RateMovie(View):
    def post(self, request, pk):
        pelicula = get_object_or_404(Pelicula, pk=pk)
        
        # Obtén los datos del formulario
        form = TuFormularioDeCalificacion(request.POST)
        
        if form.is_valid():
            calificacion = form.cleaned_data['calificacion']
            nombre_usuario = form.cleaned_data['nombre_usuario']
            reseña = form.cleaned_data['reseña']
            correo_electronico = form.cleaned_data['correo_electronico']
            edad = form.cleaned_data['edad']

            # Crear y guardar la calificación
            nueva_calificacion = Calificacion(
                pelicula=pelicula,
                calificacion=calificacion,
                nombre_usuario=nombre_usuario,
                reseña=reseña,
                correo_electronico=correo_electronico,
                edad=edad
            )
            nueva_calificacion.save()

            # Actualizar la calificación media
            pelicula.total_calificaciones += 1
            pelicula.calificacion_media = (
                (pelicula.calificacion_media * (pelicula.total_calificaciones - 1) + calificacion)
                / pelicula.total_calificaciones
            )
            pelicula.save()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

