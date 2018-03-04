# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Categoria, Curso


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
	ordering = 'position',
	list_display = 'nombre', 'position'
	list_editable = 'position',
	exclude = 'slug',

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
	pass