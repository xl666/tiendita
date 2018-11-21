from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    direccion = models.CharField(max_length=500, null=True)
    telefono = models.CharField(max_length=20, null=True)

    # Recuperar todos los productos asociados a un proveedor
    # list(proveedor.producto_set.iterator())

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    existencias = models.IntegerField()
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    proveedor = models.ForeignKey(Proveedor, null=True)

class Venta(models.Model):
    fecha = models.DateField()
    productos = models.ManyToManyField(Producto)
    total = models.DecimalField(max_digits=6, decimal_places=2)

class Prueba(models.Model):
    nombre = models.CharField(max_length=50)

    
