# -*- coding: utf-8 -*-
import datetime
import decimal
import models
from django.contrib import messages
from apps.usuarios.models import UserProfile
from apps.compras.models import Pedido
from django.shortcuts import get_object_or_404

CART_ID = 'CART-ID'


class ItemAlreadyExists(Exception):
    pass


class ItemDoesNotExist(Exception):
    pass


class Cart:
    def __init__(self, request):
        try:
            profile = UserProfile.objects.get(user__id=request.user.id)
            cart_id = profile.cart.id

        except:
            cart_id = request.session.get(CART_ID)
        if cart_id:
            try:
                cart = models.Cart.objects.get(id=cart_id, checked_out=False)
                try:
                    pedido = Pedido.objects.get(cart=cart)
                    request.session['numero_pedido'] = pedido.numero_pedido
                except:
                    request.session['numero_pedido'] = None

            except models.Cart.DoesNotExist:
                cart = self.new(request)
        else:
            cart = self.new(request)
        self.cart = cart

    def __iter__(self):
        for item in self.cart.item_set.all():
            yield item

    def new(self, request):
        cart = models.Cart(creation_date=datetime.datetime.now())
        cart.save()
        request.session[CART_ID] = cart.id
        return cart

    def add(self, product, unit_price, adicional, servicios_adicionales, quantity=1):
        try:
            print(adicional, 'tryyyy')
            item = models.Item.objects.get(
                cart=self.cart,
                product=product,
                unit_price=unit_price,
            )
        except models.Item.DoesNotExist:
            item = models.Item()
            item.cart = self.cart
            item.product = product
            # item.unit_price_base = product.base_price
            item.unit_price_base = unit_price
            item.unit_price = unit_price
            item.quantity = quantity
            item.presentacion = product.nombre
            item.producto = product.fk_producto.nombre
            if adicional is None:
                print("ADICIONAL None")
                item.precio_total_adicional = 0
            else:
                print("ADICIONAL not None")
                item.precio_total_adicional = int(adicional)
            item.save()
            for s in servicios_adicionales:
                item.sub_item.create(
                    fk_item=item,
                    nombre=s.nombre,
                    precio=s.precio,
                    num=s.id
                )
            item.save()
        else:
            # ItemAlreadyExists
            item.unit_price = unit_price
            item.quantity = item.quantity + int(quantity)
            item.save()

    def remove(self, product):
        try:
            item = models.Item.objects.get(
                cart=self.cart,
                product=product,
            )
        except models.Item.DoesNotExist:
            raise ItemDoesNotExist
        else:
            item.delete()


    def update(self, product, quantity, id_item, unit_price=None, servicios_adicionales=None):
        try:
            item = models.Item.objects.get(
                cart=self.cart,
                id=id_item,
            )
        except models.Item.DoesNotExist:
            print "entre al except"
            raise ItemDoesNotExist
        else:
            # ItemAlreadyExists
            if quantity == 0:
                item.delete()
            else:
                item.product = product
                item.unit_price = product.precio_venta
                item.quantity = int(quantity)
                if servicios_adicionales is not None:
                    for i in item.sub_item.all():
                        i.delete()
                    for s in servicios_adicionales:
                        item.sub_item.create(
                            fk_item=item,
                            nombre=s.nombre,
                            precio=s.precio,
                            num=s.id
                        )
                else:
                    pass
                item.save()

    def count(self):
        result = 0
        for item in self.cart.item_set.all():
            result += 1 * item.quantity
        return result

    def summary(self):
        result = 0
        for item in self.cart.item_set.all():
            result += item.total_price
        return result

    def summary_base(self):
        result = 0
        for item in self.cart.item_set.all():
            result += item.total_base_price
        return result

    def summary_discounts(self):
        result = 0
        for item in self.cart.item_set.all():
            result += item.total_savings
        return result

    def clear(self):
        for item in self.cart.item_set.all():
            item.delete()
