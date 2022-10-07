from django.urls import path
from django.urls import include
from rest_framework.routers import  DefaultRouter
from .import views


 


#Consumiendo APIS
router = DefaultRouter()
router.register(r"Categorias", views.CategoriaViewSet)
router.register(r"Productos", views.ProductoViewSet)

urlpatterns = [
   # Consumiendo ModelViewSet
   path('api/',include(router.urls)),
   path('api/almacen/registrar',views.AlmacenRegistrarListar.as_view(),name='Almacen de Productos'),
   path('api/almacen/actualizar/<int:pk>',views.AlmacenActualizarListar.as_view(),name='Actualizar Producto de Almacen'),
   path('productos/reporte/<int:pk>', views.reporte_productos_categoria),
    # Url cuando no consumo API
    path('listacategorias', views.Categorias, name='categorias'),
     path('nuevaCategoria', views.nuevaCategoria, name='nuevaCategoria'),
     path('editarCategoria', views.editarCategoria, name='editarCategoria'),
     path('home', views.Home,name="home")
]