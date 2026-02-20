from django import forms 
from .models import CarritoItem

class ContactoForm(forms.Form): 
    """
    Formulario independiente (no vinculado a modelo) para la sección de contacto.
    Define campos manuales para capturar información del usuario.
    """
    # Campo de texto simple para el nombre del remitente
    nombre = forms.CharField(max_length=50)
    
    # Campo con validación automática de formato de correo electrónico
    email = forms.EmailField(required=True)
    
    # Campo de texto largo usando el widget 'Textarea' para múltiples líneas
    mensaje = forms.CharField(widget=forms.Textarea)


class CrearCarritoItemForm(forms.ModelForm): 
    """
    Formulario vinculado al modelo CarritoItem.
    Se utiliza para permitir al usuario especificar la cantidad de un producto
    al momento de añadirlo a su carrito.
    """
    class Meta: 
        # Referencia al modelo de la base de datos
        model = CarritoItem
        
        # Solo exponemos el campo 'cantidad', ya que el 'producto' y el 'carrito' 
        # se asignan automáticamente en la vista (view)
        fields = ["cantidad"]