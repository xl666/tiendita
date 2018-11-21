
from rest_framework import serializers
from modelo import models

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Proveedor
        fields = ('id', 'nombre', 'pais', 'direccion', 'telefono')

class ProductoSerializer(serializers.ModelSerializer):

    def validate(self, data):
        lista = models.Producto.objects.filter(nombre=data['nombre'])
        
        if len(lista) != 0:
            raise serializers.ValidationError("El nombre del producto no puede estar repetido")

        return data
                
    
    def validate_precio(self, value):
        if value < 10:
            raise serializers.ValidationError("El precio no puede ser menor a 10")
        return value
    
    class Meta:
        model = models.Producto
        fields = ('id', 'nombre', 'existencias', 'precio', 'proveedor')


class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Venta
        fields = ('id', 'fecha', 'productos', 'total')    
        

class PruebaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Prueba
        fields = ('id', 'nombre')    
