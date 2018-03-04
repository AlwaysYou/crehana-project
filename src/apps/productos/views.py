from django.shortcuts import render
from .models import Categoria, Curso
# Create your views here.

def listado(request, slug=None):

    categorias = Categoria.objects.all().order_by('position')
    if slug == None:
        print("No hay slug")
        categoria_selected = Categoria.objects.all().order_by('position')[0]

        try:
            cursos = Curso.objects.filter(fk_categoria=categoria_selected).order_by('position')
        except:
            cursos = None
    else:
        print("hay slug")
        categoria_selected = Categoria.objects.get(slug=slug)

        # Traer los productos
        cursos = Curso.objects.filter(fk_categoria=categoria_selected).order_by('position')
    return render(request, 'productos/listado.html', locals())


