from django.urls import path
from usuarios import views as v

urlpatterns = [
    path('registro/', v.registro_usuario, name="registro"),
    path('login/', v.login_usuario, name="login"),
    path('logout/', v.logout_usuario, name="logout"),
    path('', v.inicio, name="inicio"),
    path('contacto/', v.contacto, name="contacto"),
    path('carrito/', v.ver_carrito, name="carrito"),
    path('crear_carritoItem/<int:id>', v.crear_carritoItem, name="crear_carritoItem"),
    path('eliminar_carritoItem/<int:id>', v.eliminar_carritoItem, name="eliminar_carritoItem")
]
