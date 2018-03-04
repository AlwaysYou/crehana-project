from django.db import models
from filebrowser.fields import FileBrowseField
from apps.cart.models import Cart
from apps.usuarios.models import UserProfile
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Pedido(models.Model):
    created = models.DateTimeField(editable=False, auto_now_add=True, blank=True, null=True)

    numero_pedido = models.CharField(
        'Código de Pedido',
        max_length=12,
        unique=True,
        default='00001'
    )
    precio_total = models.DecimalField(
        'Precio Total',
        max_digits=12,
        decimal_places=2,
        default=0
    )
    # Relaciones
    usuario = models.ForeignKey(
        UserProfile,
        blank=True,
        null=True,
        related_name='pedidos',
        on_delete=models.SET_NULL
    )
    cart = models.OneToOneField(
        Cart,
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )

class PedidoItem(models.Model):
    pedido = models.ForeignKey(
        Pedido,
        verbose_name='Pedido',
        related_name='pedido_item'
    )
    unit_price_base = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        verbose_name='unit base price'
    )
    unit_price = models.DecimalField(
        max_digits=18, decimal_places=2, verbose_name='unit price')
    quantity = models.PositiveIntegerField(verbose_name='Cantidad')
    # product as generic relation
    total = models.DecimalField(max_digits=18, decimal_places=2,
                                verbose_name='Total', default=0)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    fecha = models.DateTimeField(
        'Fecha de compra',
        blank=True,
        null=True,
        auto_now_add=False
    )
    producto = models.CharField(
        'Producto/Servicio',
        blank=True,
        max_length=200
    )
    presentacion = models.CharField('Presentacion', blank=True, max_length=200)

    # objects = ItemManager()

    class Meta:
        verbose_name = _('item')
        verbose_name_plural = _('items')
        ordering = ('pedido',)

    def __unicode__(self):
        return u'%d units of %s' % (self.quantity, self.product.__class__.__name__)

    @property
    def total_price(self):
        return self.quantity * self.unit_price

    @property
    def total_base_price(self):
        return self.quantity * self.unit_price_base

    @property
    def unit_savings(self):
        return self.unit_price_base - self.unit_price

    @property
    def total_savings(self):
        return self.total_base_price - self.total_price

    @property
    def discount_percentage(self):
        return (self.unit_savings * 100) / self.unit_price_base

    # product
    def get_product(self):
        return self.content_type.get_object_for_this_type(pk=self.object_id)

    def set_product(self, product):
        self.content_type = ContentType.objects.get_for_model(type(product))
        self.object_id = product.pk

    product = property(get_product, set_product)

