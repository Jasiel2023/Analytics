from django.db import models

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
    infoUsuario = models.CharField(max_length=80)
    resultadosAlmacenados = models.CharField(max_length=500)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="informe_list")
    medidorDeConsumo = models.ForeignKey(MedidorDeConsumo, on_delete=models.CASCADE, related_name="medidorDeConsumo")
    def __str__(self):
        return self.__fechaAnalisis

class registroDispositivos(models.Model):
    consumoKwh = models.FloatField()
    tiempoDeUso = models.DateField()
    cantidadDispositivos = models.IntegerField()
    def __str__(self):
        return self.consumoKwh

class DISPOSITIVOS(models.Model):
    AIRE_ACONDICIONADO = models.BooleanField()
    ASPIRADORA = models.BooleanField()
    REFRIGERADORA = models.BooleanField()
    TELEVISOR = models.BooleanField()
    CAFETERA = models.BooleanField()
    CELULAR = models.BooleanField()
    CONSOLA = models.BooleanField()
    EQUIPO_DE_SONIDO = models.BooleanField()
    DUCHA_ELECTRICA = models.BooleanField()
    FOCO = models.BooleanField()
    IMPRESORA = models.BooleanField()
    LAMPARA = models.BooleanField()
    LAPTOP = models.BooleanField()
    LAVADORA = models.BooleanField()
    LICUADORA = models.BooleanField()
    MICROONDAS = models.BooleanField()
    PLANCHA = models.BooleanField()
    ROUTER = models.BooleanField()
    SECADORA = models.BooleanField()
    TOSTADOR = models.BooleanField()
    VENTILADOR = models.BooleanField()
    DUCHA_ELECTRICA = models.BooleanField()

    def __str__(self):
        return self.AIRE_ACONDICIONADO
