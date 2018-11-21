import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from modelo import models
from modelo import serializers

client = Client()

class GetAllProductosTest(TestCase):
    def setUp(self):
        pro = models.Proveedor(nombre='patito', pais='honduras', direccion='av siempre viva', telefono='4353453')
        pro.save()
        models.Producto(nombre="cajita feliz", existencias=3, precio=10.50, proveedor=pro).save()
        models.Producto(nombre="chocolate", existencias=30, precio=22.70, proveedor=pro).save()
        models.Producto(nombre="paleta", existencias=11, precio=4.50, proveedor=pro).save()

    def test_get_all_productos(self):
        response = client.get(reverse('get_post_productos'))
        productos = models.Producto.objects.all()
        seri = serializers.ProductoSerializer(productos, many=True)
        self.assertEqual(len(productos), 3)
        self.assertEqual(response.data, seri.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class AddNewPoductoTest(TestCase):        
    def setUp(self):

        pro = models.Proveedor(nombre='patito', pais='honduras', direccion='av siempre viva', telefono='4353453')
        pro.save()
        
        self.valid_payload = {
            'nombre': 'Muffin',
            'existencias': 40,
            'precio': 40.50,
            'proveedor': pro.pk
        }
        self.invalid_payload = {
            'nombre': 'cajita feliz',
            'existencias': 4,
            'precio': 11.40,
            'proveedor': pro.pk
        }
        pr1 = models.Producto(nombre="cajita feliz", existencias=3, precio=10.50, proveedor=pro)
        pr1.save()

    def test_add_valid_producto(self):
        response = client.post(
            reverse('get_post_productos'),
            data=json.dumps(self.valid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_add_producto_existente(self):
        response = client.post(
            reverse('get_post_productos'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
