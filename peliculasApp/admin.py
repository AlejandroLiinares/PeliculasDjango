from django.contrib import admin
from .models import Pelicula

@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "año", "genero", "director")
    search_fields = ("nombre", "año")
