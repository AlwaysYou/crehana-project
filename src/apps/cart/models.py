from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType


class Cart(models.Model):
    creation_date = models.DateTimeField(verbose_name=_('creation date'))
    checked_out = models.BooleanField(default=False, verbose_name=_('checked out'))

    class Meta:
        verbose_name = _('cart')
        verbose_name_plural = _('carts')
        ordering = ('-creation_date',)

    def __str__(self):
        return '00%s' % (self.id)


class ItemManager(models.Manager):
    def get(self, *args, **kwargs):
        if 'product' in kwargs:
            kwargs['content_type'] = ContentType.objects.get_for_model(type(kwargs['product']))
            kwargs['object_id'] = kwargs['product'].pk
            del(kwargs['product'])
        return super(ItemManager, self).get(*args, **kwargs)


class Item(models.Model):
    cart = models.ForeignKey(Cart, verbose_name=_('cart'))
    quantity = models.PositiveIntegerField(verbose_name=_('quantity'))
    codigo = models.CharField(u"Código", max_length=400)
    unit_price = models.DecimalField(max_digits=18, decimal_places=2, verbose_name=_('Precio'))
    # product as generic relation
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    precio_total_adicional = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    objects = ItemManager()
    producto = models.CharField('Producto/Servicio', blank=True, max_length=200)

    class Meta:
        verbose_name = _('item')
        verbose_name_plural = _('items')
        ordering = ('cart',)

    def __str__(self):
        return u'%d units of %s' % (self.quantity, self.product.__class__.__name__)

    @property
    def total_price(self):
        return self.quantity * self.unit_price + self.precio_total_adicional

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
