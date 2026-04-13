from peliculasApp.models import Pelicula
from django.shortcuts import render,redirect
from . import forms

def index(request):
    form =forms.PeliculaForm()
    if request.method=='POST':
        form=forms.PeliculaForm(request.POST)
        if form.is_valid():
            print("Formulario OK")
            print("Nombre: ",form.cleaned_data['nombre'])
            #ver información procesada desde el form
            form.save()
            return listar_peliculas(request)
    data={'form':form}
    return render(request,'peliculasApp/index.html',data)

def listar_peliculas(request):
    peliculas = Pelicula.objects.all()
    data={'peliculas':peliculas}
    return render(request,'peliculasApp/peliculas.html',data)

def editar_pelicula(request, id):
    pelicula = Pelicula.objects.get(id=id)
    form = forms.PeliculaForm(instance=pelicula)
    if request.method == 'POST':
        form = forms.PeliculaForm(request.POST, instance=pelicula)
        if form.is_valid():
            form.save() # Aquí actualiza el registro en lugar de crear uno nuevo
        return listar_peliculas(request)#redirect('employee_list')
    else:
        data = {'form':form}
        return render(request, 'peliculasApp/index.html', data)

def eliminar_pelicula(request,id):
    pelicula=Pelicula.objects.get(id=id)
    pelicula.delete()
    return redirect('peliculas:peliculas')
