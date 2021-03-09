function showInfo() {
    info = document.getElementById("info").innerHTML.split("&lt;next&gt;");
    document.body.removeChild(document.getElementById("info"));
    divs = document.getElementsByClassName("flexDiv");
    for (let i=0; i<info.length; i++) {
        if (i!=3) {
            divs[i].children[1].innerHTML = info[i]
        }
        else {
            let text = ["Empleado", "Administrador"]
            divs[i].children[1].innerHTML = text[parseInt(info[i])]
        }
    }
}