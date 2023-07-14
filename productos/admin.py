from django.contrib import admin
from .models import Categoria, Producto


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')  # nmbres de los campos que quiero mostrar


class ProductoAdmin(admin.ModelAdmin):
    exclude = ('creado_en',)
    list_display = ('id', 'nombre', 'stock', 'puntaje', 'creado_en')

# Register your models here.


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)
