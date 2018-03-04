# -*- coding: utf-8 -*-

from django.db import models
from uuslug import uuslug
from filebrowser.fields import FileBrowseField

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField('Nombre', max_length=120)
    slug = models.SlugField('slug', max_length=180, blank=True)
    position = models.SmallIntegerField('Posición', default=0)

    def save(self, *args, **kwargs):
        try:
            for x in self.producto_presentacion.order_by('position'):
                if x.precio_base > 0:
                    self.oferta = True
        except:
            pass
        self.slug = uuslug(self.nombre, instance=self)
        super(Categoria, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.nombre


class Curso(models.Model):
    fk_categoria = models.ForeignKey(Categoria,
    							     related_name="prod_cat",
    							     verbose_name="Categoria",
    							     blank=True)

    nombre = models.CharField('Nombre del Curso', max_length=120)
    position = models.SmallIntegerField(u'Posición', default=0)
    codigo = models.CharField(u"Código", max_length=400)
    precio = models.DecimalField('Precio Referencia', max_digits=12, decimal_places=2, default=0)
    img_curso = FileBrowseField('Imagen del Curso',
                                max_length=200, blank=True,
                                extensions=['.jpg', '.png', '.gif'],
                                directory='imagen_curso')

    class Meta:
        verbose_name = u'Curso'
        verbose_name_plural = u'Curso'

    def __str__(self):
        return u'%s' % self.nombre

