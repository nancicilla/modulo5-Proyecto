from django.shortcuts import render
from django.http.response import HttpResponse
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets,generics
from rest_framework.decorators import api_view
from almacen.models import *
from .serializers import *
from django.views.defaults import page_not_found
from django.template import RequestContext

# Create your views here.

def Categorias(request):
    #listaCategoria=Categoria.objects.all().order_by('nombre').values()
    listaCategoria=CategoriaSerializer
    return render(request, "listacategorias.html",{'listaCategoria':listaCategoria})

def Home(request):
    
    return render(request, "home.html")


def index(request):
    return render(request, "almacen/index.html")    

def nuevaCategoria(request):
    categoria = request.POST.get('nombre')
    descripcion = request.POST.get('descripcion')
    if categoria:
        q = Categoria(nombre=categoria, descripcion = descripcion)
        q.save()
        
    filtro_nombre = request.GET.get("nombre")
    if filtro_nombre:
        categorias = Categoria.objects.filter(nombre__contains=filtro_nombre)
    else:
        categorias = Categoria.objects.all()
    print(categorias.query)
    return render(request, "listaCategorias.html", {"listaCategoria": categorias})

def editarCategoria(request):
    return render(request, "listaCategorias.html", {"listaCategoria":''})

class CategoriaViewSet (viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
class ProductoViewSet (viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
class AlmacenRegistrarListar(generics.CreateAPIView, generics.ListAPIView):
    queryset = Almace.objects.all()
    serializer_class = AlmaceSerializer



class AlmacenActualizarListar(generics.UpdateAPIView,generics.ListAPIView):
    queryset = Almace.objects
    serializer_class = AlmaceSerializer
    
    def patch(self,request,pk=None):
        almacen=self.queryset.filter(id=pk)
        if almacen:
            almace_serializer=self.serializer_class(almacen,many=True)
            return Response(almace_serializer.data,status=status.HTTP_200_OK)
        return Response({'error':'No existe el Almacen '},status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def reporte_productos_categoria(request,pk=None):
    """
    Reporte de productos por Categotia
    """
    
    
    try:
       
        productos = Producto.objects.filter(idcategoria=pk)
       
        cantidad = productos.count()
        
        print(JsonResponse(
            ReporteProductosSerializer({
                "cantidad": cantidad,
                "productos": productos
            }).data,
            safe=False,
            status=200,
        ))
        return JsonResponse(
            ReporteProductosSerializer({
                "cantidad": cantidad,
                "productos": productos
            }).data,
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({"mensaje": str(e) ,"pk":pk}, status=400)
def pagina_404(request,exception):
    
    response = render('404.html', {})
    response.status_code = 404
    return response
 
