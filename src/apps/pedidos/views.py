# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.decorators.http import require_POST
from apps.productos.models import Curso, Categoria
from django.shortcuts import get_object_or_404, render, redirect
from apps.usuarios.models import UserProfile
from django.core.urlresolvers import reverse, reverse_lazy

from apps.cart.cart import Cart
# Create your views here.

def mi_carrito(request):
    try:
        profile = request.user.userprofile
    except:
        print("error")
        return redirect(reverse('usuarios:user_logout'))
    if profile:
        cart = Cart(request)
        flag_mostrar_productos = False
        cantidad_items = cart.count()
        if cantidad_items > 0:
            flag_mostrar_productos = True
        items = cart.cart.item_set.all()
        items_cursos = [(item, item.get_product()) for item in items]
    return render(request, 'pedidos/mi_carrito.html', locals())


@require_POST
def add_to_cart(request):
    print("ADD")
    print(request.POST, "<- POST")
    product_id = request.POST.get('product_id')
    quantity = 1
    curso = get_object_or_404(Curso, id=product_id)
    print(curso, "<- curso")
    cart = Cart(request)
    cart.add(curso, curso.precio, quantity)
    try:
        profile = UserProfile.objects.get(user__id=request.user.id)
        print(profile, "<- profile")
        if not profile.cart:
            profile.cart = cart.cart
            profile.save()
    except:
        print("ERRORR")
        return redirect(reverse('usuarios:crear_cuenta'))


    return redirect(reverse('pedidos:mi_carrito'))


def remove_from_cart(request):
    print('VIEW: remove_from_cart')
    curso_id = request.GET.get('curso_id')
    curso_id = int(curso_id)
    curso = get_object_or_404(Curso, id=curso_id)
    cart = Cart(request)
    cart.remove(curso)
    return redirect(reverse('pedidos:mi_carrito'))