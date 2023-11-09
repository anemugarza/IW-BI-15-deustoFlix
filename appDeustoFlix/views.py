from django.shortcuts import render, get_object_or_404, get_list_or_404, HttpResponseRedirect
from django.http import HttpResponse
from .models import Genero, Pelicula, Director
from django.views import View

#devuelve el listado de generos
def index_generos(request):
	generos = get_list_or_404(Genero.objects.order_by('nombre'))
	context = {'lista_generos': generos }
	return render(request, 'generos.html', context)

#devuelve los datos de un genero
def show_genero(request, genero_id):
	genero = get_object_or_404(Genero, pk=genero_id)
	context = {'genero': genero }
	return render(request, 'genero.html', context)

#devuelve el listado de peliculas
def index_peliculas(request):
	peliculas = get_list_or_404(Pelicula.objects.order_by('nombre'))
	context = {'lista_peliculas': peliculas }
	return render(request, 'peliculas.html', context)

#devuelve los datos de una pelicula
def show_pelicula(request, pelicula_id):
	pelicula = get_object_or_404(Pelicula, pk=pelicula_id)
	context = {'pelicula': pelicula }
	return render(request, 'pelicula.html', context)

#devuelve el listado de directores
def index_directores(request):
	directores = get_list_or_404(Director.objects.order_by('nombre'))
	context = {'lista_directores': directores }
	return render(request, 'directores.html', context)

#devuelve los datos de un director
def show_director(request, director_id):
	director = get_object_or_404(Director, pk=director_id)
	context = {'director': director }
	return render(request, 'director.html', context)

#devuelve las peliculas de un genero
def peliculasGenero(request, genero_id):
	genero = Genero.objects.filter(pk=genero_id)  
	peliculasGenero = Pelicula.objects.filter(genero=genero) 
	context = {'genero': genero ,'peliculasGenero' : peliculasGenero }
	return render(request, 'peliculas.html', context)

#devuelve las peliculas de un director
def peliculasDirector(request, director_nombre):
	director = Director.objects.get(pk=director_nombre)  
	peliculasDirector = Pelicula.objects.filter(director=director) 
	context = {'director': director, 'peliculasDirector' : peliculasDirector }
	return render(request, 'peliculas.html', context)


#Devuelve la pelicula mas vista de cada genero
def indexPortada(request):
    generos = Genero.objects.all()
    peliculasMasVistas = []  # Una lista de objetos de modelo Pelicula

    for genero in generos:
        pelicula_mas_vista = Pelicula.objects.filter(genero=genero).order_by('-vecesVista').first()
        if pelicula_mas_vista:
            peliculasMasVistas.append(pelicula_mas_vista)
    context = {"lista_peliculasMasVistas": peliculasMasVistas}
    return render(request, "index.html", context)
