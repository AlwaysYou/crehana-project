from django.conf.urls import url

from . import views

app_name = 'checkout'


urlpatterns = [
    url(r'^payments/$', views.checkout, name='checkout'),

]