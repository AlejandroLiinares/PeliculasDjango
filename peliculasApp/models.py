from django.db import models

class Pelicula(models.Model):
    nombre = models.CharField(max_length=100)
    año = models.IntegerField()
    genero = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.nombre} ({self.año})"