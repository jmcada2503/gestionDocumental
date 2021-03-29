var notSecretCode = "Ñi2KSDEmkjadX{°%t(C_+|~*6r:0&5¡V/1TyZh$GFNenH?7¬.z},ñcuQ!b8;)^9pOoW=g-UvLxJPfYMw4A¿lq#BRs3I"

function sendData() {
    var send = true;

    // Check notNull elements
    var elements = document.getElementsByClassName("notNull");
    for (let i = 0; i < elements.length; i++) {
        console.log(elements[i].value)
        if (elements[i].value == "") {
            console.log("Prueba")
            elements[i].style.backgroundColor = "rgb(255, 217, 217)";
            elements[i].style.border = "2px solid rgb(255, 187, 187)";
            send = false;
        }
        else {
            elements[i].style.backgroundColor = "white";
            elements[i].style.border = "1px solid gray  ";
        }
    }

    if (send) {
        //Check password
        passwordElements = Array.from(document.getElementsByClassName("inputText")).slice(-3, -1);
        if (passwordElements[0].value != passwordElements[1].value) {
            alert("Las contraseñas deben ser iguales");
        }
        else {
            var notAccepted = "";
            for (let i=0; i<passwordElements[0].value.length; i++) {
                if (notSecretCode.indexOf(passwordElements[0].value[i]) == -1) {
                    send = false
                    notAccepted += passwordElements[0].value[i]+", ";
                }
            }
            if (send) {
                if (document.getElementsByName("age")[0].value != "" && parseInt(document.getElementsByName("age")[0].value) == NaN) {
                    alert("La edad debe ser un número entero")
                }
                else {
                    document.getElementById("formDataUser").submit();
                }
            }
            else {
                alert("No se admiten los siguientes caractéres dentro de las contraseñas: ( "+notAccepted.substring(0, notAccepted.length-2)+" )");
            }
        }
    }
    else {
        alert("No puedes dejar estos campos vacíos")
    }
}