$document.ready(function(){
    console.log(ahora)
    obtenerListaAros();

});

function obtenerListaAros(){
    console.log("AQUI")
    $.get({
        url:'http://127.0.0.1:8000/api/Aro/',
        success: function(listado){
            console.log(listado)

        },
        error: function(error){
            console.error("Error en el servidor de aros")
        }
    })

}