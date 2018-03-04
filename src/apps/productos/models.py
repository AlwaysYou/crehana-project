# -*- coding: utf-8 -*-

from django.db import models
from uuslug import uuslug

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField('Nombre', max_length=120)
    slug = models.SlugField('slug', max_length=180, blank=True)
    position = models.SmallIntegerField('Posición', default=0)

    class Meta:
        abstract = True

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
