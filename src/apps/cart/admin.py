# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Cart, Item


class ItemInline(admin.StackedInline):
    model = Item

    extra = 0


@admin.register(Cart)
class CartTarjetaAdmin(admin.ModelAdmin):
    inlines = [ItemInline, ]
