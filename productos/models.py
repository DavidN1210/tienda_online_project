from django.db import models

# Create your models here.

class Producto(models.Model):
    """
    Modelo que representa un producto individual en el catálogo de la tienda.
    Almacena información básica como nombre, marca, descripción y precio.
    """
    # Nombre del producto con un límite de 50 caracteres
    nombre = models.CharField(max_length=50)
    
    # Marca del fabricante o proveedor
    marca = models.CharField(max_length=50)
    
    # Descripción detallada (blank=False y null=False obligan a escribir algo)
    descripcion = models.TextField(blank=False, null=False)
    
    # Precio del producto representado con decimales
    precio = models.FloatField()

    def __str__(self):
        """
        Retorna el nombre del producto como su representación en texto,
        lo cual facilita su identificación en el panel de administración.
        """
        return self.nombre