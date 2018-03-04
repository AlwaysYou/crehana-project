from django.contrib import admin

from .models import (Pedido, PedidoItem)
# Register your models here.

class PedidoItemInline(admin.StackedInline):
    model = PedidoItem
    exclude = ['content_type', 'object_id', ]
    extra = 0

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
	pass
