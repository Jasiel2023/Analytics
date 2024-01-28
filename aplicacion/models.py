from enum import Enum
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=90)
    cedula = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Registro(models.Model):
    registro = models.CharField(max_length=80)
    dispositivos = models.ForeignKey(DISPOSITIVOS, on_delete=models.CASCADE, related_name="registro")
    def __str__(self):
        return self.registro

class MedidorDeConsumo(models.Model):
    consumoTotal = models.FloatField()
    registro = models.ForeignKey(Registro, on_delete=models.CASCADE, related_name="medidorDeConsumo")
    def __str__(self):
        return self.consumoTotal

class Informe(models.Model):
    fechaAnalisis = models.DateField()

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #resultadosAlmacenados = models.CharField(max_length=500)
   # usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="informe_list")
   # medidorDeConsumo = models.ForeignKey(MedidorDeConsumo, on_delete=models.CASCADE, related_name="medidorDeConsumo")
    def __str__(self):
        return self.user.username

class registroDispositivos(models.Model):
    consumoKwh = models.FloatField()
    tiempoDeUso = models.DateField()
    cantidadDispositivos = models.IntegerField()
    def __str__(self):
        return self.consumoKwh

#class Dispositivos(Enum):
 #   AIRE_ACONDICIONADO = models.BooleanField(False)
    #  ASPIRADORA = models.BooleanField(False)
    #   REFRIGERADORA = models.BooleanField(False)
    #TELEVISOR = models.BooleanField(False)
    #CAFETERA = models.BooleanField(False)
    #CELULAR = models.BooleanField(False)
    #CONSOLA = models.BooleanField(False)
    #EQUIPO_DE_SONIDO = models.BooleanField(False)
    #DUCHA_ELECTRICA = models.BooleanField(False)
    #FOCO = models.BooleanField(False)
    #IMPRESORA = models.BooleanField(False)
    #LAMPARA = models.BooleanField(False)
    #LAPTOP = models.BooleanField(False)
    #LAVADORA = models.BooleanField(False)
    #LICUADORA = models.BooleanField(False)
    #MICROONDAS = models.BooleanField(False)
    # PLANCHA = models.BooleanField(False)
    #ROUTER = models.BooleanField(False)
    #SECADORA = models.BooleanField(False)
    #TOSTADOR = models.BooleanField(False)
    #VENTILADOR = models.BooleanField(False)

#class RegistroDeDispositivos(models.Model):
    #   dispositivo = models.CharField(max_length=20, choices=[(tag.name, tag.value) for tag in Dispositivos])

#   def __str__(self):
#       return self.dispositivo



