from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from productos.models import Producto
from usuarios.models import Carrito, CarritoItem
from .forms import ContactoForm, CrearCarritoItemForm
from django.contrib.auth.decorators import login_required 
from django.contrib import messages 

def registro_usuario(request):
    """
    Vista de registro de usuarios.
    - GET: muestra el formulario de registro.
    - POST: valida credenciales, crea el usuario y redirige al login.
    """
    if request.method == "POST":
        # Se procesa el formulario con los datos enviados
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Se guarda el nuevo usuario en la base de datos
            usuario = form.save()
            messages.success(request, "Usuario registrado con éxito")
            return redirect("login")
    else:
        # Se envía un formulario de registro vacío
        form = UserCreationForm()

    return render(request, "usuarios/registro.html", {"form": form})


def login_usuario(request):
    """
    Vista de inicio de sesión.
    - GET: muestra el formulario de login.
    - POST: valida credenciales y crea la sesión del usuario.
    """
    if request.method == "POST":
        # AuthenticationForm requiere el objeto request y los datos POST
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Se extrae el usuario validado del formulario
            usuario = form.get_user()
            # Se crea la sesión en el navegador
            login(request, usuario)
            messages.success(request, "Has iniciado sesión correctamente")
            return redirect("inicio")
    else:
        # Formulario de login vacío
        form = AuthenticationForm()

    return render(request, "usuarios/login.html", {"form": form})


def logout_usuario(request):
    """
    Vista de cierre de sesión.
    Elimina la sesión del usuario actual y redirige al login.
    """
    # Elimina los datos de sesión del usuario
    logout(request)
    messages.success(request, "Has cerrado sesión correctamente")
    return redirect("login")


def contacto(request):
    """
    Vista de gestión de contacto.
    - GET: muestra el formulario de contacto.
    - POST: valida y redirige con mensaje de éxito si los datos son correctos.
    """
    if request.method == "POST":
        mi_formulario = ContactoForm(request.POST)
        if mi_formulario.is_valid():
            messages.success(request, "El formulario de contacto ha sido enviado con éxito")
            return redirect("inicio")
    else:
        mi_formulario = ContactoForm()

    return render(request, "usuarios/contacto.html", {"form": mi_formulario})


def ver_carrito(request):
    """
    Vista para visualizar el contenido del carrito del usuario.
    Obtiene o crea un carrito para el usuario y filtra sus ítems asociados.
    """
    # Se busca el carrito del usuario; si no existe, se crea uno nuevo
    carrito, creado = Carrito.objects.get_or_create(user=request.user)
    # Se obtienen todos los productos añadidos a ese carrito
    items = CarritoItem.objects.filter(carrito=carrito)
    return render(request, "usuarios/carrito.html", {"items": items})


@login_required
def crear_carritoItem(request, id):
    """
    Vista para añadir un producto específico al carrito.
    Requiere que el usuario esté autenticado.
    Asocia el ítem con el carrito del usuario y el producto seleccionado.
    """
    carrito, creado = Carrito.objects.get_or_create(user=request.user)
    producto = Producto.objects.get(id=id)

    if request.method == "POST":
        form = CrearCarritoItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.carrito = carrito
            item.producto = producto
            item.save()
            messages.success(request, "Producto añadido al carrito con éxito")
            return redirect("carrito")
    else:
        form = CrearCarritoItemForm()

    return render(request, "usuarios/crear_carritoItem.html", {
        "form": form,
        "carrito": carrito,
        "producto": producto
    })


def eliminar_carritoItem(request, id):
    """
    Vista para eliminar un ítem del carrito.
    Tras eliminarlo, actualiza la lista de ítems y renderiza el carrito de nuevo.
    """
    # Se obtiene el ítem por su ID
    carrito_item = CarritoItem.objects.get(id=id)
    carrito = carrito_item.carrito
    # Se borra el registro de la base de datos
    carrito_item.delete()
    # Se refresca la lista de ítems restantes para la respuesta
    items = CarritoItem.objects.filter(carrito=carrito) 
    messages.success(request, "Los productos elegidos han sido eliminados del carrito con éxito")
    return render(request, "usuarios/carrito.html", {"items": items})


def inicio(request):
    """
    Vista de la página principal.
    Muestra un mensaje de bienvenida personalizado y la lista total de productos.
    """
    # Lógica para personalizar el saludo según el estado de la sesión
    if request.user.is_authenticated:
        mensaje = f"Hola, {request.user.username}"
    else:
        mensaje = "No has iniciado sesión"
    
    # Obtención de todos los productos disponibles
    productos = Producto.objects.all()

    return render(request, "usuarios/inicio.html", {"mensaje": mensaje, "productos": productos})