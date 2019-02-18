from django.db import models
from django.conf import settings
from django.contrib.auth.models import Group

# Create your models here.

class Projecte(models.Model):
    nom =  models.CharField(max_length=200, help_text="Nom")
    descripcio = models.TextField(blank=True, null=True, default="Un nou projecte")
    scrumMaster = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="scrumMaster" )
    productOwner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, 
        related_name="productOwner" )
    grup = models.ForeignKey(Group,
    on_delete = models.CASCADE)
    def __str__(self):
        return self.nom


class Sprint(models.Model):
    projecte = models.ForeignKey(Projecte,
    on_delete=models.CASCADE )
    data_inici = models.DateField();
    data_final = models.DateField();
    hores = models.IntegerField(default=0, help_text="Hores disponibles blablabla..")

class Spec(models.Model):
    DIFICULTAT = (
        ("D","Desconeguda"),
        ("B","Baixa"),
        ("M","Mitjana"),
        ("A","Alta")
        )
    descripcio = models.TextField();
    dificultat = models.CharField(max_length=1,choices=DIFICULTAT, default="D");
    hores = models.IntegerField(default=0);
    developer = models.ForeignKey(settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True, blank=True )
    sprint = models.ForeignKey(Sprint,
        on_delete=models.CASCADE,
        null=True, blank=True )
    projecte =  models.ForeignKey(Projecte,
        on_delete=models.CASCADE )
