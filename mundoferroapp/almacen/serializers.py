from rest_framework import serializers
from .models import Categoria,Producto,Almace

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Categoria
        fields = "__all__"
class ProductoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Producto
        fields = "__all__"
class AlmaceSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Almace
        fields = "__all__"
class ReporteProductosSerializer(serializers.Serializer):
    cantidad = serializers.IntegerField()
    productos = ProductoSerializer(many=True)