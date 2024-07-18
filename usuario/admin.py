from django.contrib import admin
from .models import Producto, Usuario, Precio,Categoría,Supermercado
# Register your models here.

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display=('ID_Producto', 'Nombre_Produc')
    ordering = ('ID_Producto',)
    search_fields = ('Nombre_Produc',)
    list_display_links = ('ID_Producto',)
    list_per_page = 10
    exclude = ('Nombre_Produc',)

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display=('ID_Usuario', 'Nombre_User', 'Fechar_registro', 'Correo')
    ordering = ('ID_Usuario',)
    search_fields = ('Correo',)
    list_display_links = ('ID_Usuario',)
    list_per_page = 10
    exclude = ('Correo', 'Fechar_registro',)

@admin.register(Precio)
class PrecioAdmin(admin.ModelAdmin):
    list_display = ('ID_Precio', 'Precio_Prod')  # Eliminar 'Fecha_registro'
    ordering = ('ID_Precio',)
    search_fields = ('ID_Precio',)  # Eliminar 'Fecha_registro'
    list_display_links = ('ID_Precio',)
    list_per_page = 10
    # Eliminar la línea de 'exclude'

@admin.register(Categoría)
class CategoríaAdmin(admin.ModelAdmin):
    list_display=('ID_Categoría', 'Nombre_Catego')
    ordering = ('ID_Categoría',)
    search_fields = ('Nombre_Catego',)
    list_display_links = ('ID_Categoría',)
    list_per_page = 10
    exclude = ('Nombre_Catego',)

@admin.register(Supermercado)
class SupermercadoAdmin(admin.ModelAdmin):
    list_display=('ID_Supermercado', 'Nombre_tienda')   
    ordering = ('ID_Supermercado',)
    search_fields = ('Nombre_tienda',)
    list_display_links = ('ID_Supermercado',)
    list_per_page = 10
    exclude = ('Nombre_tienda',)