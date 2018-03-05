from django.db import models

# Create your models here.

class InformacionGeneral(models.Model):

    site = models.CharField("URL del sitio", max_length=60, blank=True,
        help_text='Ingrese la url actual del sitio sin el slash final')
    email = models.EmailField('Email Para correos')
    taxi = models.DecimalField(u'Taxi por Envío', max_digits=12, decimal_places=2, default=0)

    class Meta:
        verbose_name = u'Información General'
        verbose_name_plural = u'Información General'

    def __str__(self):
        return u'Información del Sitio'