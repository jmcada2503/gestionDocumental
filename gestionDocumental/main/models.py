from django.db import models

# Create your models here.
class user(models.Model):
    idCode = models.CharField(max_length=10, primary_key=True, null=False)
    idCard = models.FileField(upload_to="documents", null=True)
    name = models.CharField(max_length=30, null=False)
    lastName = models.CharField(max_length=30, null=False)
    rol = models.SmallIntegerField(null=False)
    phoneNumber = models.CharField(max_length=10, null=True)
    password = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=50, null=True)
    eps = models.CharField(max_length=30, null=True)
    edad = models.IntegerField(null=True)
    profession = models.CharField(max_length=50, null=True)
    signedIn = models.CharField(max_length=20, null=True)
    verified = models.SmallIntegerField(default=0, null=False)

    def getInfo(self):
        return "{}<next>{}<next>{}<next>{}<next>{}<next>{}<next>{}<next>{}<next>{}".format(self.name, self.lastName, self.idCode, self.rol, self.phoneNumber, self.eps, self.email, self.edad, self.profession)

    def __str__(self):
        return """
idCode:{}
name:{}
lastName:{}
rol:{}
phoneNumber:{}
password:{}
email:{}
eps:{}
edad:{}
profession:{}
signedIn:{}
verified:{}
""".format(self.idCode, self.name, self.lastName, self.rol, self.phoneNumber, self.password, self.email, self.eps, self.edad, self.profession, self.signedIn, self.verified)