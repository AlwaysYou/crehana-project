from django.shortcuts import render
from apps.productos.models import Categoria, Curso
# Create your views here.
from apps.cart.cart import Cart


def home(request):
    cursos = Curso.objects.filter(
        mostrar_home=True).order_by('position')

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
    return render(request, 'web/home.html', locals())



