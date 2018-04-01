# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.decorators.http import require_POST
from apps.productos.models import Curso, Categoria
from django.shortcuts import get_object_or_404, render, redirect
from apps.usuarios.models import UserProfile
from django.core.urlresolvers import reverse, reverse_lazy
from .utils import get_next_codigo_pedido
from apps.cart.cart import Cart
from .forms import PedidoForm
from apps.web.models import InformacionGeneral
from apps.pedidos.models import Pedido

# Paquetes para la respuesta JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
# Create your views here.

def mi_carrito(request):
    header = "mi_carrito"
    try:
        profile = request.user.userprofile
    except:
        """ Logout si no existe userprofile """
        return redirect(reverse('usuarios:user_logout'))

    """ Si existe el profile, obtenemos el cart de ese profile"""
    if profile:
        cart = Cart(request)
        flag_mostrar_productos = False
        cantidad_items = cart.count()
        if cantidad_items > 0:
            flag_mostrar_productos = True
        items = cart.cart.item_set.all()
        items_cursos = [(item, item.get_product()) for item in items]

    # Suma para el precio final
    _subtotal = cart.summary()
    info_general = InformacionGeneral.objects.get(pk=1)
    taxi = info_general.taxi
    if taxi:
        total = _subtotal + taxi
    else:
        total = _subtotal
    """ Bloque para pago """
    # Consultamos al numero de pedido
    if request.method == 'POST':
        print("Soy POST")
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.cart = cart.cart
            pedido.usuario = profile
            pedido.numero_pedido = get_next_codigo_pedido()
            pedido.precio_total = total
            profile.cart = None
            profile.save()
            pedido.save()
            return redirect(reverse('pedidos:gracias'))
        else:
            print(form.errors, "<- errores!!!")
    return render(request, 'pedidos/mi_carrito.html', locals())


@csrf_exempt
def mi_carrito_pago(request):
    print("ENTRO")
    profile = request.user.userprofile
    data = {'status': 'error'}
    cart = Cart(request)
    # Suma para el precio final
    _subtotal = cart.summary()
    info_general = InformacionGeneral.objects.get(pk=1)
    taxi = info_general.taxi
    if taxi:
        total = _subtotal + taxi
    else:
        total = _subtotal
    """ Bloque para pago """
    # Consultamos al numero de pedido
    if request.method == 'POST':
        print("Soy POST")
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.cart = cart.cart
            pedido.usuario = profile
            pedido.numero_pedido = get_next_codigo_pedido()
            pedido.precio_total = total
            del request.session['CART-ID']
            profile.cart = None
            profile.save()
            pedido.save()
        else:
            print(form.errors, "<- errores!!!")
    else:
        print("NO SOY  POST")
    return JsonResponse(data)


@require_POST
def add_to_cart(request):
    product_id = request.POST.get('product_id')
    quantity = 1
    curso = get_object_or_404(Curso, id=product_id)
    cart = Cart(request)
    cart.add(curso, curso.precio, quantity)
    try:
        profile = UserProfile.objects.get(user__id=request.user.id)
        print(profile, "<- profile")
        if not profile.cart:
            profile.cart = cart.cart
            profile.save()
    except:
        return redirect(reverse('usuarios:login'))

    return redirect(reverse('pedidos:mi_carrito'))


def remove_from_cart(request):
    print('VIEW: remove_from_cart')
    curso_id = request.POST.get('product_id')
    curso_id = int(curso_id)
    curso = get_object_or_404(Curso, id=curso_id)
    cart = Cart(request)
    cart.remove(curso)
    return redirect(reverse('pedidos:mi_carrito'))

def gracias(request):
    try:
        profile = UserProfile.objects.get(user__id=request.user.id)
        pedidos_from_user = Pedido.objects.filter(usuario=profile).order_by('-created')[0]
    except:
        pedidos_from_user = None
    print(pedidos_from_user, "<- get_last_pedido")

    return render(request, 'pedidos/gracias.html', locals())
