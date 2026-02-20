# Practica 2 - Django - Proyecto Tienda Online
## Descripción del proyecto
Este proyecto consiste en una tienda online que adapta su comportamiento según el estado de autenticación del usuario. 
Dependiendo de si el usuario ha iniciado sesión o no, las funcionalidades disponibles cambian para ofrecer una experiencia personalizada.

Si el usuario no esta autenticado:
* Solo puedes ver los detalles del producto con el botón ver, una tabla con todos los productos y acceder al formulario de contacto
* Se habilitan los botones/enlaces de registro y iniciar sesión
* Se indica en un título que no has iniciado sesión

Si el usuario está autenticado:
* Aparece indicado en un titulo que has iniciado sesíon con un saludo al usuario correspondiente
* Desaparecen los botones/enlaces de registro y login por el botón de cerrar sesión
* Además de lo que podias hacer cuando no habías iniciado sesión (ver los detalles del producto...), ahora puedes eliminar y crear tus propios productos.
* Se añade un carrito en el que se registrarán los pedidos de cada usuario. Dentro del carrito puedes ver y eliminar tus pedidos.

## Guía de ejecución del proyecto
### 1. Preparar el entorno virtual
``` bash
python -m venv entorno_django
source entorno_django/bin/activate  # En Windows: venv\Scripts\activate
```
### 2. Instalar dependencias
``` bash
pip install django
```
### 3. Iniciar el servidor
Iniciar el servidor dentro de la carpeta del proyecto con el entorno activado
``` bash
python manage.py runserver
```
## Tecnologías utilizadas
* Backend: Django
* Base de datos: SQLite 
* Diseño y interactividad: HTML, CSS y JavaScript
* Estilos: Bootstrap 5
