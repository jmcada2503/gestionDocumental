function action(select) {
    id = document.createElement("input");
    id.className = "variable";
    id.name = "id";
    id.type = "text";
    id.value = document.getElementsByName("idCode")[0].placeholder;
    document.getElementById("modifyUser").appendChild(id);
    action = document.createElement("input");
    action.type = "text";
    action.className = "variable";
    action.name = "action";
    action.value = select;
    document.getElementById("modifyUser").appendChild(action);
    document.getElementById("modifyUser").submit();
}

function verifyButton() {
    if (document.getElementById("v").innerHTML == "1") {
        document.getElementById("navbarButtons").getElementsByClassName("textButton")[0].remove()
        document.getElementById("navbarButtons").getElementsByClassName("spaceBar")[0].remove()
    }
}

function disableLink() {
    console.log("Prueba")
    label = document.querySelector("label[for='idCard']");
    if (label.children[0].href == window.location.href) {
        label.innerHTML = label.children[0].innerHTML;
        label.style.color = "gray";
    }
}