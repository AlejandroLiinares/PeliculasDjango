from django.urls import path
from . import views

app_name="peliculas"

urlpatterns=[
    path('',views.index,name="agregar"),
    path('peliculas/',views.listar_peliculas,name='peliculas'),
    path('actualizarPelicula/<int:id>',views.editar_pelicula,name="editar"),
    path('eliminarPelicula/<int:id>',views.eliminar_pelicula,name='eliminar'),
]

