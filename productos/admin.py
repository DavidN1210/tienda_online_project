from django.contrib import admin
from .models import Producto

# Register your models here.

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    """
    Configuración personalizada para el modelo Producto en el panel de administración.
    Define cómo se listan, buscan y ordenan los registros.
    """
    
    # Columnas que se mostrarán en la tabla principal del administrador
    list_display = ('nombre', 'marca', 'precio')
    
    # Crea una barra de búsqueda que filtra por estos campos específicos
    search_fields = ('nombre', 'marca')
    
    # Establece el orden por defecto (alfabéticamente por nombre)
    ordering = ('nombre',)