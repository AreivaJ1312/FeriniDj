function validarFormulario(){
    //remover el mensaje de error(el div)
    $('.alert').remove();

    //declaración de variables 
    var nombre=$('#nombre').val(),
        apellido=$('#apellido').val(),
        email=$('#email').val(),
        sugerenciaConsulta=$('#sugerenciaConsulta').val(),
        comunas=$('#comunas').val(),
        areaText=$('#areaText').val(),
        mensj=$('#mensj').val();

    
        //validacion del campo nombre
    if(nombre=="" || nombre==null){
        cambiarColor("nombre");
        mostrarAlerta("Campo obligatorio *nombre");
        return false;
    }else{
        var expresion= /^[a-zA-ZñÑáéíóúÁÉÍÓÚ ]*$/;
        if(!expresion.test(nombre)){
            cambiarColor(nombre);
            mostrarAlerta("No se permiten caracteres especiales o números");

        }
    }

    //validacion apellido (cambio de color y caract. especiales)
    if(apellido=="" || apellido==null){
        cambiarColor("apellido");
        mostrarAlerta("Campo obligatorio *apellido");
        return false;
    }else{
        var expresion=  /^[a-zA-ZñÑáéíóúÁÉÍÓÚ ]*$/;
        if(!expresion.test(apellido)){
            cambiarColor(apellido);
            mostrarAlerta("No se permiten caracteres especiales o números");

        }
    }

    //validacion correo(cambio color y caract. especiales)
    if(email=="" || email==null){
        cambiarColor("email");
        mostrarAlerta("Campo obligatorio *email");
        return false;
    }else{
        var expresion= /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/;
        if(!expresion.test(email)){
            cambiarColor(email);
            mostrarAlerta("Por favor ingresar un correo válido");

        }
    }

//Validacion para campo no vacio sugerencias y consultas

    if(sugerenciaConsulta=="" || sugerenciaConsulta==null ||sugerenciaConsulta=="..."){
        cambiarColor("sugerenciaConsulta");
        mostrarAlerta("Campo obligatorio *Sugerencia o consulta");
        return false;
    }
    


//validacion para campo no vacio comunas

    if(comunas=="" || comunas==null ||comunas=="..."){
        cambiarColor("comunas");
        mostrarAlerta("Campo obligatorio *comunas");
        return false;
    }

//validacion para campo no vacio en areatext

    if(areaText=="" || areaText==null ){
        cambiarColor("areaText");
        mostrarAlerta("Campo obligatorio *mensaje");
        return false;
    }



}
//funcion para cambiar el color cuando este mal
function cambiarColor(dato){
    $('#' + dato).css({
        border: "1px solid #dd5144"
    });

}
// funcion de mostrar alerta
function mostrarAlerta(texto){
    $('#mensj').before('<div class="alert">Error: '+ texto +'</div>');
}
