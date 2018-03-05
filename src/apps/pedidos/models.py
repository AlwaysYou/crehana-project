from django.db import models
from filebrowser.fields import FileBrowseField
from apps.cart.models import Cart
from apps.usuarios.models import UserProfile
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Pedido(models.Model):
    created = models.DateTimeField(editable=False, auto_now_add=True, blank=True, null=True)
    estado = models.CharField("Estado", max_length=400)
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



