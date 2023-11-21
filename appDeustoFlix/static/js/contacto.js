// Muestra una alerta en el navegador informando de que el mensaje ha sido recibido.
$(document).ready(
    function () {
        document.getElementById("btn_enviar").onclick = function () {
            window.alert("Su mensaje ha sido recibido. Nos pondremos en contacto con usted.");
        };
    }
);

