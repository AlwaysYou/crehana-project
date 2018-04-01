from django.shortcuts import get_object_or_404, render, redirect
from django.core.urlresolvers import reverse
from apps.cart.cart import Cart
from apps.web.models import InformacionGeneral

# Create your views here.


def checkout(request):
    header = "mi_carrito"
    try:
        profile = request.user.userprofile
    except:
        """ Logout si no existe userprofile """
        return redirect(reverse('usuarios:user_logout'))

    """ Si existe el profile, obtenemos el cart de ese profile"""
    if profile:
        cart = Cart(request)
        # Suma para el precio final
        _subtotal = cart.summary()
        info_general = InformacionGeneral.objects.get(pk=1)
        taxi = info_general.taxi
    if taxi:
        total = _subtotal + taxi
    else:
        total = _subtotal
    return render(request, 'checkout/checkout.html', locals())


