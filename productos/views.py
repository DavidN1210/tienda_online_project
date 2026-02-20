from django.shortcuts import render, redirect
from .forms import CrearProductoForm
from django.contrib.auth.decorators import login_required 
from .models import Producto
from django.contrib import messages 

@login_required
def crear_producto(request):
    """
    Vista para la creación de un nuevo producto.
    Requiere que el usuario esté autenticado.
    Si es POST: Valida y guarda el formulario.
    Si es GET: Muestra el formulario vacío.
    """
    if request.method == "POST":
        # Se cargan los datos del formulario enviado
        form = CrearProductoForm(request.POST)
        if form.is_valid():
            # Guarda el objeto en la base de datos
            form.save()
            # Agrega un mensaje de éxito para el usuario
            messages.success(request, "El producto ha sido creado con éxito")
            # Redirige a la página de inicio tras la creación
            return redirect("inicio")
    else:
        # Instancia un formulario limpio para mostrarlo
        form = CrearProductoForm()

    return render(request, "productos/crear_producto.html", {"form": form})


def ver_producto(request, id):
    """
    Vista para visualizar los detalles de un producto específico.
    Recibe el 'id' del producto desde la URL.
    """
    # Busca el producto por su clave primaria (id)
    producto = Producto.objects.get(id=id)
    # Renderiza el template de detalle pasando el objeto producto
    return render(request, "productos/ver_producto.html", {"producto": producto})


@login_required
def eliminar_producto(request, id):
    """
    Vista para eliminar un producto de la base de datos.
    Requiere autenticación y el 'id' del producto.
    Tras eliminar, redirige al inicio con un mensaje confirmatorio.
    """
    # Obtiene el objeto que se desea borrar
    producto = Producto.objects.get(id=id)
    # Ejecuta la eliminación en la base de datos
    producto.delete()
    # Notifica al usuario que el borrado fue exitoso
    messages.success(request, "El producto elegido ha sido eliminado con éxito")
    # Redirige a la vista principal
    return redirect("inicio")