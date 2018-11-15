"Este es un archivo de configuración para la versión 1.11 de django"


"""tiendita URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from tiendita.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^proveedores/', Proveedores.as_view()),
    url(r'proveedor/(?P<pk>\d+)/', Proveedor_detalle.as_view()),
    url(r'^productos/', Productos.as_view()),
    url(r'producto/(?P<pk>\d+)/', Producto_detalle.as_view()),
    url(r'^ventas/', Ventas.as_view()),
    url(r'venta/(?P<pk>\d+)/', Venta_detalle.as_view()),
]
