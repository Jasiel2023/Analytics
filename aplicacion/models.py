from django.contrib.auth.models import User
from django.db import models

class Registro(models.Model):
    registro = models.CharField(max_length=80)

    def __str__(self):
        return self.registro

from django.db import models
class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cedula = models.CharField(max_length=10, blank=True, null=True)
    gmail = models.EmailField(blank=True, null=True)
    direccion = models.TextField()
    def __str__(self):
        return self.user.username
class MedidorDeConsumo(models.Model):
    consumoTotal = models.FloatField()
    registro = models.ForeignKey(Registro, on_delete=models.CASCADE, related_name="medidorDeConsumo")
    def __str__(self):
        return self.consumoTotal

class Informe(models.Model):

    fechaAnalisis = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class registroDispositivos(models.Model):
    consumoKwh = models.FloatField()
    tiempoDeUso = models.DateField()
    cantidadDispositivos = models.IntegerField()

    def __str__(self):
        return self.consumoKwh

class Dispositivo(models.Model):
    # Campos de texto
    nombre_dispositivo = models.CharField(max_length=255)
    cantidad_dispositivo = models.FloatField()
    cantidad_consumo = models.FloatField()
    consumo_hora = models.FloatField()
    total_energia = models.FloatField(default=0.0)
    fecha_registro = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_dispositivo


