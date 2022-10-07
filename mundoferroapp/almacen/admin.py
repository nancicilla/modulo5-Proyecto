from django.contrib import admin
from django import forms
from .models import Categoria,Producto,Fabricante
# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):   
    def get_form(self, request, obj=None, **kwargs):
     #--> Get form 
        form = super().get_form(request, obj, **kwargs)
     #--> Add placeholder for field
        form.base_fields['nombre'].widget.attrs['placeholder'] = "Nombre de la Categoria..."
     #--> Return form
        return form
class FabricanteAdmin(admin.ModelAdmin):   
    def get_form(self, request, obj=None, **kwargs):
     #--> Get form 
        form = super().get_form(request, obj, **kwargs)
     #--> Add placeholder for field
        form.base_fields['nombre'].widget.attrs['placeholder'] = "Nombre del Fabricante..."
     #--> Return form
        return form
class ProductoAdmin(admin.ModelAdmin):   
    def get_form(self, request, obj=None, **kwargs):
     #--> Get form 
        form = super().get_form(request, obj, **kwargs)
     #--> Add placeholder for field
        form.base_fields['nombre'].widget.attrs['placeholder'] = "Nombre del Producto..."
     #--> Return form
        return form
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Fabricante,FabricanteAdmin)
admin.site.register(Producto,ProductoAdmin)