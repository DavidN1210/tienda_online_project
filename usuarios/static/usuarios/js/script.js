// Seleccionamos todos los botones cuyo ID comienza con 'btn_eliminar'
let botonesEliminar = document.querySelectorAll('[id^="btn_eliminar"]');

botonesEliminar.forEach(btn => {
    btn.addEventListener('click', function(event) {
        // Pregunta sencilla al usuario
        let respuesta = confirm("¿Estás seguro de que quieres eliminar esto?");
        
        if (!respuesta) {
            // Si cancela, evitamos que el enlace (href) funcione
            event.preventDefault();
        }
    });
});