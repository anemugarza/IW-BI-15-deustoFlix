from email.policy import default
from django.db import models

# Create your models here.
class Genero(models.Model):
    nombre = models.CharField(max_length=70)  # Nombre del género
     # Este género es apto para todos = True, si no lo es = False
    apto_para_todos =  (models.BooleanField(default=False))

    def __str__(self) -> str:
        return self.nombre


class Director(models.Model):
    nombre = models.CharField(max_length=70)  # Nombre de la oferta
    fecha_nacimiento = models.DateField()  
    nacionalidad = models.CharField(max_length=70)
    premiado = (models.BooleanField(default=False))
    imagen = models.ImageField(upload_to='img',blank=True,null=True,verbose_name='Image')


    def __str__(self) -> str:
        return self.nombre
        
class Pelicula(models.Model):
    nombre = models.CharField(max_length=70)  #Nombre de la película
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)  # Género de la película
    director = models.ManyToManyField(Director)    
    fecha_estreno = models.DateField()  
    duracion = models.IntegerField()
    recomendacionEdad = models.IntegerField()  
    vecesVista = models.IntegerField()  
    imagen = models.ImageField(upload_to='img',blank=True,null=True,verbose_name='Image')


    def __str__(self) -> str:
        return self.nombre
