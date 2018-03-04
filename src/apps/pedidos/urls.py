from django.conf.urls import url

from . import views

app_name = 'pedidos'


urlpatterns = [
    url(r'^mi-carrito/$', views.mi_carrito, name='mi_carrito'),
]