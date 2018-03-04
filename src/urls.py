
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from apps.usuarios import urls as usuarios_urls
from apps.productos import urls as productos_urls
from apps.web import urls as web_urls

ADMIN_URL = settings.ADMIN_URL

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include(web_urls, namespace='web')),
    url(r'^usuarios/', include(usuarios_urls, namespace='usuarios')),
    url(r'^productos/', include(usuarios_urls, namespace='productos')),


] + (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) +
     static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))