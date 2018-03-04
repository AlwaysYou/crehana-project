import datetime
from .models import Cart as Cart_model
from .models import Item as Item_model
from django.contrib import messages
from apps.pedidos.models import Pedido
from apps.usuarios.models import UserProfile

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
            print("El profile cuenta con Cart id")
        except:
            cart_id = request.session.get(CART_ID)
            print("Except - Init, El cart_id es:", cart_id)

        if cart_id:
            try:
                # Si existe en la base de datos, lo cojemos
                print("Existe el cart_id - entro al if")
                cart = Cart_model.objects.get(id=cart_id, checked_out=False)
                try:
                    pedido = Pedido.objects.get(cart=cart)
                    request.session['numero_pedido'] = pedido.numero_pedido
                    print("HAY CART_ID SE ASOCIA A ALGUN PEDIDO // CART LINEA 39 Y GUARDAMOS EN SESION EL NUMERO DEL PEDIDO")
                except:
                    request.session['numero_pedido'] = None
                    print("No hay cart, no se asocia a ningun pedido")
            except Cart_model.DoesNotExist:
                # Si no existe, lo creamos
                cart = self.new(request)
            # Si Cart_id = None
        else:
            cart = self.new(request)
        # Usaremos el self.cart mas abajo
        self.cart = cart

    def __iter__(self):
        for item in self.cart.item_set.all():
            yield item

    def new(self, request):
        # Crea, guarda y almacena en session
        cart = Cart_model(creation_date=datetime.datetime.now())
        cart.save()
        request.session[CART_ID] = cart.id
        return cart

    def add(self, product, unit_price, quantity=1):
        try:
            item = Item_model.objects.get(
                cart=self.cart,
                product=product,
            )
        except Item_model.DoesNotExist:
            item = Item_model()
            item.cart = self.cart
            item.product = product
            item.unit_price = unit_price
            item.quantity = quantity
            item.producto = product.nombre
            item.save()
        else:
            # ItemAlreadyExists
            item.unit_price = unit_price
            item.quantity = item.quantity + int(quantity)
            item.save()

    def remove(self, product):
        try:
            item = Item_model.objects.get(
                cart=self.cart,
                product=product,
            )
        except Item_model.DoesNotExist:
            raise ItemDoesNotExist
        else:
            item.delete()

    def update(self, product, quantity, unit_price=None):
        try:
            item = Item_model.objects.get(
                cart=self.cart,
                product=product,
            )
        except Item_model.DoesNotExist:
            raise ItemDoesNotExist
        else:
            # ItemAlreadyExists
            if quantity == 0:
                item.delete()
            else:
                item.unit_price = unit_price
                item.quantity = int(quantity)
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
