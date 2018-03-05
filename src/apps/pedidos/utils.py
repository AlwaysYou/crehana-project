# -*- coding: utf-8 -*-

from .models import Pedido


def get_next_codigo_pedido():
    ultimo_pedido = Pedido.objects.all().order_by('numero_pedido').last()
    if not ultimo_pedido:
        return '00001'
    numero_pedido = ultimo_pedido.numero_pedido
    numero_pedido_int = int(numero_pedido)
    nuevo_numero_pedido_int = numero_pedido_int + 1
    nuevo_numero_pedido = str(nuevo_numero_pedido_int)
    nuevo_numero_pedido = nuevo_numero_pedido.zfill(5)
    return nuevo_numero_pedido
