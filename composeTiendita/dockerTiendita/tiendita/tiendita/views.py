from django.http import HttpResponse
from modelo import models
from modelo import serializers
from django.http import JsonResponse
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from rest_framework import mixins
from rest_framework import generics


class Proveedores(generics.ListCreateAPIView):
    queryset = models.Proveedor.objects.all()
    serializer_class = serializers.ProveedorSerializer
    

class Proveedor_detalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Proveedor.objects.all()
    serializer_class = serializers.ProveedorSerializer

class Productos(generics.ListCreateAPIView):
    queryset = models.Producto.objects.all()
    serializer_class = serializers.ProductoSerializer

class Producto_detalle(generics.RetrieveUpdateAPIView):
    queryset = models.Producto.objects.all()
    serializer_class = serializers.ProductoSerializer


class Ventas(generics.ListCreateAPIView):        
    queryset = models.Venta.objects.all()
    serializer_class = serializers.VentaSerializer

class Venta_detalle(generics.RetrieveUpdateAPIView):        
    queryset = models.Venta.objects.all()
    serializer_class = serializers.VentaSerializer
