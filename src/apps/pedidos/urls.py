from django.conf.urls import url

from . import views

app_name = 'pedidos'


urlpatterns = [
    url(r'^mi-carrito/$', views.mi_carrito, name='mi_carrito'),
    url(r'^agregar-producto/$', views.add_to_cart, name='add_to_cart'),

]