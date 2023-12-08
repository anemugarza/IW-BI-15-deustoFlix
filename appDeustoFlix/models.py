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
    calificacion = models.FloatField(default=0.0)
    nombre_usuario = models.CharField(max_length=100, blank=True)
    reseña = models.TextField(blank=True)
    calificacion_media = models.DecimalField(default=0.0,max_digits=3,decimal_places=2)
    total_calificaciones = models.PositiveIntegerField(default=0)
    calificaciones = models.ManyToManyField('Calificacion', related_name='peliculas')
    correo_electronico = models.EmailField(blank=True, null=True)
    edad = models.PositiveIntegerField(blank=True, null=True)

    def actualizar_calificacion(self, nueva_calificacion):

        if hasattr(self, 'calificaciones'):
            self.calificaciones.append(nueva_calificacion)
        else:
            self.calificaciones = [nueva_calificacion]

        self.calificacion_media = sum(self.calificaciones) / len(self.calificaciones)

        # Guardar el objeto actualizado en la base de datos
        self.save()
    def __str__(self) -> str:
        return self.nombre
    
class Calificacion(models.Model):
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE, related_name='calificaciones_pelicula')
    calificacion = models.FloatField()
    nombre_usuario = models.CharField(max_length=100)
    reseña = models.TextField(blank=True, null=True)
    correo_electronico = models.EmailField(blank=True, null=True)
    edad = models.IntegerField(blank=True, null=True)
