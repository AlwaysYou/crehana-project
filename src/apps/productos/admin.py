# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Categoria, Curso
from filebrowser.settings import ADMIN_THUMBNAIL


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
	ordering = 'position',
	list_display = 'nombre', 'position'
	list_editable = 'position',
	exclude = 'slug',

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = 'nombre', 'fk_categoria', 'miniatura', 'mostrar_home', 'position'
    list_editable = 'position',
    ordering = 'position',
    list_filter = "fk_categoria__nombre",
    def miniatura(self, obj):
        try:
            if obj.img_curso.path and obj.img_curso.filetype == "Image":
                return "<img src='%s'>" % obj.img_curso.version_generate(
                    ADMIN_THUMBNAIL).url
            else:
                return ""
        except:
            return ""
    miniatura.allow_tags = True
    miniatura.short_description = "Imagen Derecha Miniatura"
