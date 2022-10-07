from email.policy import default
from importlib.util import module_from_spec
from pyexpat import model
from random import choices
from secrets import choice
import this
from unittest.util import _MAX_LENGTH
from django.db import models
from django.conf import settings
from .validators import *
# Create your models here.
class Categoria(models.Model):
    nombre=models.CharField(max_length=100,unique=True,validators=[validar_longitudnombre,])
    descripcion=models.TextField()
    idcategoria=models.ForeignKey('self',models.SET_NULL, blank=True, null=True,related_name="categoria",verbose_name="Categoria")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombre
    
class Fabricante(models.Model):
    nombre=models.CharField(max_length=100,unique=True,validators=[validar_longitudnombre,])
    telefonos=models.TextField(verbose_name="Teléfono(s)")
    responsable=models.TextField(verbose_name="Responsable(s)")
    direccion=models.TextField()
    correo=models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombre
    
class ProductUnits(models.TextChoices):
    UNITS = 'u', 'Unidades'
    KG = 'kg', 'Kilogramos'
    L='l','Litros'
    
class Producto(models.Model):
    nombre=models.CharField(max_length=100,unique=True,validators=[validar_longitudnombre,])
    codigo=models.CharField(max_length=100,null=True)
    archivo = models.ImageField(upload_to='images/',verbose_name="Fotografía")
    unidades = models.CharField(max_length=2, 
                                choices= ProductUnits.choices,
                                default=ProductUnits.UNITS)
    descuento= models.FloatField(default=0,validators=[validar_descuento,],verbose_name="Descuento(%)") # desduento en porcentaje
    descripcion=models.TextField()
    idcategoria=models.ForeignKey(Categoria,on_delete=models.CASCADE,related_name="categoria_producto",verbose_name="Categoria")
    idfabricante=models.ForeignKey(Fabricante,on_delete=models.CASCADE,related_name="fabricante",verbose_name="Fabricante")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombre
class  Almace(models.Model):
   
    cantidad=models.IntegerField(validators=[validar_cantidad,])
    fecharegistro=models.DateField(verbose_name="Fecha de Compra")
    preciounitariocompra=models.DecimalField(max_digits=10,decimal_places=2,validators=[validar_precio,],verbose_name="Precio de Compra")
    preciounitarioventa=models.DecimalField(max_digits=10, decimal_places=2 ,validators=[validar_precio,],verbose_name="Precio de Venta")
    idproducto=models.ForeignKey(Producto,on_delete=models.CASCADE,verbose_name="Producto")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
   
    
class Estado(models.TextChoices):
    PA = 'pa', 'Pagado'
    PE = 'pe', 'Pendiente'   
    
class Cliente(models.Model):
    nombre= models.CharField(max_length=200,validators=[validar_longitudnombre,])
    correo= models.EmailField()
    contrasenia=models.TextField()
    
class CarritoCompra(models.Model):
    idcliente =models.ForeignKey(Cliente,null=True, on_delete=models.CASCADE,related_name="cliente",verbose_name="Cliente")
    estado= models.CharField(max_length=2, choices=Estado.choices, default=Estado.PA)
    fechaEntrega= models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class DetalleCarritoCompra(models.Model):
    idProducto=models.ForeignKey(Producto, on_delete=models.CASCADE,related_name="detalle",verbose_name="Producto")
    cantidad=models.IntegerField(validators=[validar_cantidad,])
    precio=models.FloatField(validators=[validar_precio,])
    idCarritoCompra=models.ForeignKey(CarritoCompra, on_delete=models.CASCADE,related_name="carrito",verbose_name="Carrito de Compras")
    
    