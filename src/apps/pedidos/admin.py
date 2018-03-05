from django.contrib import admin
from django.core import urlresolvers

from .models import (Pedido)
# Register your models here.

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = 'numero_pedido', 'usuario', 'created', 'ver_detalle_pedido'
    exclude = 'cart',

    def ver_detalle_pedido(self, obj):
        url_change_password = urlresolvers.reverse('admin:cart_cart_change', args=(obj.cart.pk,))
        # url_change_password = urlresolvers.reverse('admin:auth_user_password_change', kwargs={'user_id': obj.id})

        return "<a href='%s'> %s </a>" % (url_change_password, u'Ver detalle del Pedido')
    ver_detalle_pedido.allow_tags = True
    ver_detalle_pedido.short_description = u'Detalle Pedido'