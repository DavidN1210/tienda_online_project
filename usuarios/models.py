from django.db import models
from django.contrib.auth.models import User 
from productos.models import Producto
from django.db import models
from django.contrib.auth.models import User 
from productos.models import Producto

# Create your models here.

class Carrito(models.Model):
    """
    Modelo que representa el carrito de compras de un usuario.
    Utiliza una relación OneToOneField para asegurar que cada usuario 
    tenga un único carrito asociado.
    """
    # Si el usuario se elimina, su carrito también se borra (CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self): 
        """Retorna una representación legible del carrito."""
        return f"Carrito de {self.user.username}"
    

class CarritoItem(models.Model):
    """
    Modelo que representa un producto específico dentro de un carrito.
    Permite gestionar la cantidad de un mismo producto sin duplicar entradas.
    """
    # Relación muchos a uno: un carrito puede tener muchos ítems
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    
    # Relación muchos a uno: un producto puede estar en muchos carritos
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    
    # Almacena la cantidad del producto (siempre positiva, por defecto 1)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        """Retorna la cantidad y el nombre del producto del ítem."""
        return f"{self.cantidad} x {self.producto.nombre}"