function confirmarEliminacion(id){
    Swal.fire({
        title: '¿Estas seguro?',
        text: "No prodrás deshacer esta acción!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Sí, Eliminar!'
      }).then((result) => {
        if (result.isConfirmed) {
          //redirigir al usuario a la ruta de eliminar
          window.location.href="eliminar_aro/"+id;
          
        }
      })
}