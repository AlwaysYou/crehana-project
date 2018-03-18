from django.conf.urls import url

from . import views

app_name = 'pedidos'


urlpatterns = [
    url(r'^mi-carrito/$', views.mi_carrito, name='mi_carrito'),
    url(r'^agregar-producto/$', views.add_to_cart, name='add_to_cart'),
    url(r'^remover-producto/$', views.remove_from_cart, name='remove_from_cart'),
    url(r'^gracias/$', views.gracias, name='gracias'),
    url(r'^mi-carrito-pago/$', views.mi_carrito_pago, name='mi_carrito_pago'),
    

]