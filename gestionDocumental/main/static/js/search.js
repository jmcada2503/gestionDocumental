usersJoined = document.getElementById("usersInfo").innerHTML.split("&lt;verified&gt;");
for (let j=0; j<usersJoined.length; j++) {
    if (usersJoined[j]!="") {
        users = usersJoined[j].split("&lt;end&gt;");
        for (let i=0; i<users.length; i++) {
            info = users[i].split("&lt;next&gt;");
        
            //flexDiv
            flexDiv = document.createElement("div");
            flexDiv.className = "flexDiv contentUserInfo";
            flexDiv.onclick = selectUser;
            
            //name
            userName = document.createElement("p");
            userName.className = "userInfo";
            userName.style["width"] = "38%";
            userName.innerHTML = info[0];
            if (j==0) {
                userName.style["color"] = "rgb(255, 115, 115)";
            }
            
            //email
            email = document.createElement("p");
            email.className = "userInfo";
            email.style["width"] = "50%";
            email.style["text-align"] = "center";
            email.innerHTML = info[1];
            if (j==0) {
                email.style["color"] = "rgb(255, 115, 115)";
            }
            
            //idCode
            idCode = document.createElement("p");
            idCode.className = "userInfo";
            idCode.style["width"] = "10%";
            idCode.style["text-align"] = "right";
            idCode.innerHTML = info[2];
            if (j==0) {
                idCode.style["color"] = "rgb(255, 115, 115)";
            }
            
            //spaceBar
            spaceBar = document.createElement("div");
            spaceBar.className = "spaceBar";
            spaceBar.style["background-color"] = "black";
            spaceBar.style["height"] = "25px";
            spaceBar.style["margin"] = "10px 0px";
            if (j==0) {
                spaceBar.style["background-color"] = "rgb(255, 115, 115)";
            }
            
            //spaceBar2
            spaceBar2 = document.createElement("div");
            spaceBar2.className = "spaceBar";
            spaceBar2.style["background-color"] = "black";
            spaceBar2.style["height"] = "25px";
            spaceBar2.style["margin"] = "10px 0px";
            if (j==0) {
                spaceBar2.style["background-color"] = "rgb(255, 115, 115)";
            }
            
            //add elements to the document
            flexDiv.appendChild(userName);
            flexDiv.appendChild(spaceBar);
            flexDiv.appendChild(email);
            flexDiv.appendChild(spaceBar2);
            flexDiv.appendChild(idCode);
        
            document.getElementById("users").appendChild(flexDiv);
        }
    }
}

function selectUser() {
    idCode = document.createElement("input");
    idCode.className = "variable";
    idCode.type = "text";
    idCode.name = "selectedUser";
    idCode.value = this.children[4].innerHTML;
    document.querySelector("form.variable").target = "_blank";
    document.querySelector("form.variable").appendChild(idCode);
    document.querySelector("form.variable").submit();
}

function refreshInfo(button) {

    button.animate([{transform: "rotate(360deg)"}], {duration: 250});

    let datos = new FormData(document.getElementById("searchUser"));
    fetch("/refreshInfo/", {
        method: "POST",
        body: datos
    })
    .then(function(res) {
        return res.text();
    })
    .then(function(data) {
        document.getElementById("users").innerHTML = "";
        usersJoined = data.split("<verified>");
        for (let j=0; j<usersJoined.length; j++) {
            if (usersJoined[j]!="") {
                users = usersJoined[j].split("<end>");
                for (let i=0; i<users.length; i++) {
                    info = users[i].split("<next>");
                
                    //flexDiv
                    flexDiv = document.createElement("div");
                    flexDiv.className = "flexDiv contentUserInfo";
                    flexDiv.onclick = selectUser;
                    
                    //name
                    userName = document.createElement("p");
                    userName.className = "userInfo";
                    userName.style["width"] = "38%";
                    userName.innerHTML = info[0];
                    if (j==0) {
                        userName.style["color"] = "rgb(255, 115, 115)";
                    }
                    
                    //email
                    email = document.createElement("p");
                    email.className = "userInfo";
                    email.style["width"] = "50%";
                    email.style["text-align"] = "center";
                    email.innerHTML = info[1];
                    if (j==0) {
                        email.style["color"] = "rgb(255, 115, 115)";
                    }
                    
                    //idCode
                    idCode = document.createElement("p");
                    idCode.className = "userInfo";
                    idCode.style["width"] = "10%";
                    idCode.style["text-align"] = "right";
                    idCode.innerHTML = info[2];
                    if (j==0) {
                        idCode.style["color"] = "rgb(255, 115, 115)";
                    }
                    
                    //spaceBar
                    spaceBar = document.createElement("div");
                    spaceBar.className = "spaceBar";
                    spaceBar.style["background-color"] = "black";
                    spaceBar.style["height"] = "25px";
                    spaceBar.style["margin"] = "10px 0px";
                    if (j==0) {
                        spaceBar.style["background-color"] = "rgb(255, 115, 115)";
                    }
                    
                    //spaceBar2
                    spaceBar2 = document.createElement("div");
                    spaceBar2.className = "spaceBar";
                    spaceBar2.style["background-color"] = "black";
                    spaceBar2.style["height"] = "25px";
                    spaceBar2.style["margin"] = "10px 0px";
                    if (j==0) {
                        spaceBar2.style["background-color"] = "rgb(255, 115, 115)";
                    }
                    
                    //add elements to the document
                    flexDiv.appendChild(userName);
                    flexDiv.appendChild(spaceBar);
                    flexDiv.appendChild(email);
                    flexDiv.appendChild(spaceBar2);
                    flexDiv.appendChild(idCode);
                
                    document.getElementById("users").appendChild(flexDiv);
                }
            }
        }
    });
}