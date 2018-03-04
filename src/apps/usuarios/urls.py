from django.conf.urls import url

from . import views

app_name = 'usuarios'


urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^create-account/$', views.crear_cuenta, name='crear_cuenta'),
]