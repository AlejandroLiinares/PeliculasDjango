from django import forms
from django.core import validators
from peliculasApp.models import Pelicula

class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ['nombre', 'año', 'genero', 'director']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'año': forms.TextInput(attrs={'class': 'form-control'}),
            'genero': forms.TextInput(attrs={'class': 'form-control'}),
            'director': forms.TextInput(attrs={'class': 'form-control'}),
        }

nombre = forms.CharField(
    min_length=5,
    max_length=30,
    validators=[
    validators.MinLengthValidator(5),
    validators.MaxLengthValidator(30),
    ],
    widget=forms.TextInput(attrs={'class': 'form-control'})
 )
 
def clean_nombre(self):
    inputNombre = self.cleaned_data['nombre']
    if inputNombre == "El cien pies humano":
        raise forms.ValidationError("No se aceptan más peliculas bizarras jaja")
    return inputNombre