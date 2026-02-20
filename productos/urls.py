from django.urls import path
from productos import views as v

urlpatterns = [
    path('crear_producto/', v.crear_producto, name="crear_producto"),
    path('ver_producto/<int:id>', v.ver_producto, name="ver_producto"),
    path('eliminar_producto/<int:id>', v.eliminar_producto, name="eliminar_producto")
]
