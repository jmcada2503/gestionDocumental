from django.shortcuts import render
from django.http import HttpResponse
from main.models import user
from random import randint

secretCode = "!~48-ZbD6ñarPVz1c¿Q.X=KYSdv/U0Fsi7AOLj^fCx?np+l&JR%;T{,5H°yq¡B2Mu3IEÑ)kN:¬_|otwW $e}mh*G9(g#"

def decode(idCode, password):
    n = 0
    for i in idCode:
        n+=int(i)

    ans = ""
    for i in password:
        c = secretCode.index(i)-n
        while c < 0:
            c += len(secretCode)
        ans += secretCode[c]
    return ans
    

def encode(idCode, text):
    n = 0
    for i in idCode:
        n+=int(i)

    password = ""
    for i in text:
        c = secretCode.index(i)+n
        while c >= len(secretCode):
            c -= len(secretCode)
        password += secretCode[c]
    return password


def notNull(s):
    if s == "":
        return None
    else:
        return s


def getRandomCode():
    r = ""
    for i in range(30):
        r += secretCode[randint(0, len(secretCode)-1)]
    return r


def getUsersInfo(query):
    users = ""
    verified = query.filter(verified=1)
    notVerified = query.filter(verified=0)
    for i in range(len(notVerified)-1, -1, -1):
        users+="{}<next>{}<next>{}<end>".format(notVerified[i].name+" "+notVerified[i].lastName, notVerified[i].email, notVerified[i].idCode)
    users = users[:-5]
    users+="<verified>"
    for i in range(len(verified)-1, -1, -1):
        users+="{}<next>{}<next>{}<end>".format(verified[i].name+" "+verified[i].lastName, verified[i].email, verified[i].idCode)
    if users == "<verified>":
        return users
    return users[:-5]


def registrarDatos(request):
    if request.method == "POST":

        if (len(user.objects.filter(idCode=request.POST.get("idCode")))==0):

            try:
                # Encriptar contraseña
                if (request.POST.get("password") == request.POST.get("checkPassword")):
                    password = encode(request.POST.get("idCode"), request.POST.get("password"))
                    
                # Validar edad
                age = notNull(request.POST.get("age"))
                try:
                    age = int(age)
                except:
                    pass

                # Validar documento de identidad
                try:
                    idCard = request.FILES["idCard"]
                except KeyError:
                    idCard = None

                # Validar número de teléfono
                if (request.POST.get("phone") != ""):
                    int(request.POST.get("phone"))

                # Registrar datos
                p = user(request.POST.get("idCode"), idCard, request.POST.get("name"), request.POST.get("lastname"), 0, notNull(request.POST.get("phone")), password, notNull(request.POST.get("email")), notNull(request.POST.get("eps")), age, notNull(request.POST.get("profession")))
                p.save()
            except ValueError:
                return render(request, "main/templates/main.html", {"error":"ERROR: Los datos fueron ingresados de manera incorrecta, el usuario no ha sido guardado en el sistema"})

            return render(request, "main/templates/redirect.html", {"page": "/"})
        
        else:
            return render(request, "main/templates/main.html", {"error":"ERROR: Este número de documento ya está registrado"})

    return render(request, "main/templates/main.html")

def signIn(request):
    if request.method == "POST":
        if (request.POST.get("rc") == None):
            if not("'" in request.POST.get("idCode") or "\"" in request.POST.get("idCode")):
                try:
                    p = user.objects.get(idCode=request.POST.get("idCode"))
                    if (decode(p.idCode, p.password) == request.POST.get("password")):
                        if (p.verified == 1):
                            r = getRandomCode()
                            p.signedIn = r
                            p.save()
                            if (p.rol == 1):
                                return render(request, "main/templates/adminPage.html", {"name":(p.name+" "+p.lastName), "rc":r+"<and>"+p.idCode, "info":p.getInfo})
                            else:
                                return render(request, "main/templates/userPage.html", {"name":(p.name+" "+p.lastName), "rc":r+"<and>"+p.idCode,  "info":p.getInfo})
                        else:
                            return render(request, "main/templates/signIn.html", {"error":"ERROR: Este usuario no ha sido verificado por un administrador"})
                    else:
                        return render(request, "main/templates/signIn.html", {"error":"ERROR: Contraseña incorrecta"})
                        
                except user.DoesNotExist:
                    return render(request, "main/templates/signIn.html", {"error":"ERROR: Este usuario no existe"})
        else:
            rc = request.POST.get("rc").split("<and>")
            p = user.objects.get(idCode=rc[1])
            if p.signedIn == rc[0]:
                if (p.rol == 1):
                    return render(request, "main/templates/adminPage.html", {"name":(p.name+" "+p.lastName), "rc":p.signedIn+"<and>"+p.idCode, "info":p.getInfo})
                else:
                    return render(request, "main/templates/userPage.html", {"name":(p.name+" "+p.lastName), "rc":p.signedIn+"<and>"+p.idCode,  "info":p.getInfo})
            else:
                 return render(request, "main/templates/redirect.html", {"page":"/"})

    return render(request, "main/templates/signIn.html")


def search(request):
    if (request.method == "POST"):
        if (request.POST.get("rc")):
            rc = request.POST.get("rc").split("<and>")
            p = user.objects.get(idCode=rc[1])
            if p.signedIn == rc[0]:
                if request.POST.get("selectedUser") != None:
                    # pasarle la información del usuario en la página en la que puede modificar sus datos

                    try:
                        usuario = user.objects.get(idCode=request.POST.get("selectedUser"))
                    except:
                        return HttpResponse("<h1>ERROR: Este usuario no existe</h1>")

                    if usuario.rol == 1:
                        rol = "Administrador"
                    else:
                        rol = "Empleado"

                    if (usuario.idCard.name != ''):
                        idCard = usuario.idCard.url
                    else:
                        idCard = ""

                    return render(request, "main/templates/modifyUser.html", {"rc":request.POST.get("rc"), "name":(usuario.name+" "+usuario.lastName), "nombre":usuario.name, "lastName":usuario.lastName, "idCode":usuario.idCode, "phoneNumber":usuario.phoneNumber, "email":usuario.email, "eps":usuario.eps, "password":decode(usuario.idCode, usuario.password), "edad":usuario.edad, "profession":usuario.profession, "rol":rol, "verified":usuario.verified, "idCard":idCard})
                elif request.POST.get("searchInput") != None:
                    keyWords = request.POST.get("searchInput").split(" ")
                    users = []
                    for i in keyWords:
                        u = []
                        u+=list(user.objects.filter(idCode=i))
                        u+=list(user.objects.filter(name__icontains=i))
                        u+=list(user.objects.filter(lastName__icontains=i))
                        for j in u:
                            if not(j in users):
                                users.append(j.idCode)
                    u = user.objects.filter(idCode__in=users)
                    return render(request, "main/templates/search.html", {"rc":request.POST.get("rc"), "usersInfo":getUsersInfo(u)})
                else:
                    return render(request, "main/templates/search.html", {"rc":request.POST.get("rc"), "usersInfo":getUsersInfo(user.objects.all())})
            else:
                return render(request, "main/templates/adminPage.html", {"error":"ERROR: Hubo un problema accediendo a esta página ;)", "name":(p.name+" "+p.lastName), "rc":rc[0]+"<and>"+p.idCode, "info":p.getInfo})

    return render(request, "main/templates/redirect.html", {"page":"/"})


def modify(request):
    if request.POST:
        if (request.POST.get("rc")):
            rc = request.POST.get("rc").split("<and>")
            p = user.objects.get(idCode=rc[1])
            if p.signedIn == rc[0]:
                if (request.POST.get("action") == "deleteUser"):
                    user.objects.get(idCode=request.POST.get("id")).idCard.delete()
                    user.objects.get(idCode=request.POST.get("id")).delete()
                elif (request.POST.get("action") == "verify"):
                    p = user.objects.get(idCode=request.POST.get("id"))
                    p.verified = 1
                    p.save()
                elif (request.POST.get("action") == "changeRol"):
                    p = user.objects.get(idCode=request.POST.get("id"))
                    if (p.rol == 1):
                        p.rol = 0
                    else:
                        p.rol = 1
                    p.save()
                elif (request.POST.get("action") == "saveInfo"):
                    p = user.objects.get(idCode=request.POST.get("id"))
                    for i in range(1, len(p.__dict__)):
                        if (request.POST.get(list(p.__dict__.keys())[i]) != "" and request.POST.get(list(p.__dict__.keys())[i]) != None):
                            if (list(p.__dict__.keys())[i] != "password"):
                                p.__dict__[list(p.__dict__.keys())[i]] = request.POST.get(list(p.__dict__.keys())[i])
                    try:
                        request.FILES["idCard"]
                        p.idCard.delete()
                        p.idCard = request.FILES["idCard"]
                    except KeyError:
                        pass
            
                    p.save()

                    if (request.POST.get("password") != "" and  request.POST.get("password") != None):
                        p.password = encode(p.idCode, request.POST.get("password"))

                    p.save()

                return render(request, "main/templates/closeTab.html")