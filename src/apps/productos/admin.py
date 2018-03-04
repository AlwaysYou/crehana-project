# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Categoria, Curso


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
	pass


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
	pass