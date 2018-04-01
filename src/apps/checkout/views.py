from django.shortcuts import get_object_or_404, render, redirect
from django.core.urlresolvers import reverse
from apps.cart.cart import Cart
from apps.web.models import InformacionGeneral
from django.conf import settings
import culqipy

# Create your views here.

culqi_public_key = settings.ENV.get("CULQI_PUBLIC_KEY")
culqi_secret_key = settings.ENV.get("CULQI_SECRET_KEY")

culqipy.public_key = culqi_public_key
culqipy.secret_key = culqi_secret_key


def checkout(request):
    culqi_public_key = settings.ENV.get("CULQI_PUBLIC_KEY")

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


