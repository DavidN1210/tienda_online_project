from django.contrib import admin
from .models import Carrito, CarritoItem

# Register your models here.

@admin.register(Carrito)
class CarritoAdmin(admin.ModelAdmin):
    """
    Configuración para el modelo Carrito en el panel de administración.
    Permite gestionar los carritos vinculados a cada usuario de la plataforma.
    """
    # Muestra el nombre de usuario asociado al carrito en la lista principal
    list_display = ('user',)
    
    # Permite buscar carritos escribiendo el nombre del usuario
    search_fields = ('user__username',) # Se recomienda usar __username para buscar por el texto del nombre
    
    # Ordena los carritos alfabéticamente según el usuario
    ordering = ('user',)

@admin.register(CarritoItem)
class CarritoItemAdmin(admin.ModelAdmin):
    """
    Configuración para el modelo CarritoItem en el panel de administración.
    Permite ver el detalle de cada producto añadido, su cantidad y a qué carrito pertenece.
    """
    # Muestra tres columnas: el dueño del carrito, el producto y la cantidad elegida
    list_display = ('carrito', 'producto', 'cantidad')
    
    # Facilita la búsqueda por el nombre del usuario dueño del carrito
    search_fields = ('carrito__user__username',)
    
    # Ordena los ítems agrupándolos por carrito
    ordering = ('carrito',)