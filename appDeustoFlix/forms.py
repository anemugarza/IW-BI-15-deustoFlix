# En forms.py
from django import forms

class TuFormularioDeCalificacion(forms.Form):
    calificacion = forms.FloatField(label='Calificación (0-10)', min_value=0, max_value=10, required=True)
    nombre_usuario = forms.CharField(label='Nombre', max_length=100, required=True)
    reseña = forms.CharField(label='Reseña (opcional)', widget=forms.Textarea, required=False)
    edad = forms.IntegerField(label='Edad', min_value=0, required=True)
    correo_electronico = forms.EmailField(label='Correo Electrónico', max_length=100, required=True)
