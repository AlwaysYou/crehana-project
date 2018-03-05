from django.shortcuts import render, redirect
from .models import Categoria, Curso
from django.core.urlresolvers import reverse
# Create your views here.
from apps.cart.cart import Cart

def listado(request, slug=None):
    header = "producto"

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

    """ Validador para que un curso solo pueda ser clickeable
        1 vez """
    try:
        profile = request.user.userprofile
    except:
        profile = None
    if profile:
        cart = Cart(request)
        items = cart.cart.item_set.all()
        list_id_items = []
        for row in items:
            list_id_items.append(row.object_id)
    return render(request, 'productos/listado.html', locals())


def buscar(request):
    busqueda = request.GET.get('palabra_magica')
    if busqueda:
        try:
            cursos = Curso.objects.filter(
                name__icontains=busqueda).order_by('position')
            if len(cursos) > 0:
                return render(request, 'productos/listado.html', locals())
            else:
                return redirect(reverse('web:home'))

        except ValueError:
            return redirect(reverse('web:home'))

