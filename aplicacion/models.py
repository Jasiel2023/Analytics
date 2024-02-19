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

class DispositivoEnum(Enum):
    AIRE_ACONDICIONADO = 'Aire Acondicionado'
    ASPIRADORA = 'Aspiradora'
    REFRIGERADORA = 'Refrigeradora'
    TELEVISOR = 'Televisor'
    CAFETERA = 'Cafetera'
    CELULAR = 'Celular'
    CONSOLA = 'Consola'
    EQUIPO_DE_SONIDO = 'Equipo De Sonido'
    DUCHA_ELECTRICA = 'Ducha Electrica'
    FOCO = 'Foco'
    IMPRESORA = 'Impresora'
    LAMPARA = 'Lampara'
    LAPTOP = 'Laptop'
    LAVADORA = 'Lavadora'
    LICUADORA = 'Licuadora'
    BATIDORA= 'Batidora'
    MICROONDAS = 'Microondas'
    TOSTADOR = 'Tostador'
    PLANCHA = 'Plancha'
    ROUTER = 'Router'
    SECADORA = 'Secadora'
    VENTILADOR = 'Ventilador'

class RegistroDeDispositivos(models.Model):
    dispositivo = models.CharField(
        max_length=50,
        choices=[(tag.name, tag.value) for tag in DispositivoEnum]
    )

    def __str__(self):
        return self.dispositivo




