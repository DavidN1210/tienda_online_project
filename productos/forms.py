from django import forms 
from .models import Producto 

class CrearProductoForm(forms.ModelForm): 
    """
    Formulario vinculado al modelo Producto.
    Permite la creación y validación automática de campos basándose 
    en la estructura definida en el modelo.
    """
    class Meta: 
        # Especifica el modelo que se utilizará para crear el formulario
        model = Producto 
        
        # Define los campos del modelo que serán visibles y editables en el formulario
        fields = ["nombre", "marca", "descripcion", "precio"]