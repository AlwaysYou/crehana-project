from django.conf.urls import url

from . import views

app_name = 'productos'


urlpatterns = [
    url(r'^listado/$', views.listado, name='listado'),
    url(r'^(?P<slug>[\w-]+)/$', views.listado, name='curso_select'),

]