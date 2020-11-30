
$(document).ready(function(){
    console.log("ahora")
    obtenerListaAros();

});

function obtenerListaAros(){
    
    $.get({
        url:'http://127.0.0.1:8000/api/Aro/',
        success: function(respuesta){
            var contenedor = $('#contenedor-galeria');
            contenedor.empty();

            if(respuesta.count == 0){

                contenedor.removeClass('card-columns')
                var alerta = $('<div></div>').addClass('alert alert-light')
                alerta.attr('role', 'alert')
                alerta.html("No hay ningun <strong>Aros<strong>")

                contenedor.append(alerta)
            } else {
                var listaAros = respuesta.results
                rellenarAros(contenedor, listaAros)

            }
        },
        error: function(error){
            console.error("Error en el servidor de aros")
            var contenedor= $('#contenedor-productos')
            contenedor.empty();
            contenedor.removeClass('card-columns')

            var alerta = $('<div></div>').addClass('alert alert-danger')
            alert.attr('role','alert')
            alert.html("Error con el servicio de Aros")

            contenedor.append(alerta)

            console.error("error con el servicio de rescatados");
            console.error(error);
        }
    })

}

function rellenarAros(contenedor,){
    var contenedor= $('#contenedor-productos')
}