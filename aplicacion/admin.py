from django.contrib import admin
from .models import Usuario
from .models import Informe
from .models import MedidorDeConsumo
from .models import Registro
from .models import registroDispositivos
from .models import DISPOSITIVOS
# Register your models here.
admin.site.register(Usuario)
admin.site.register(Informe)
admin.site.register(MedidorDeConsumo)
admin.site.register(Registro)
admin.site.register(DISPOSITIVOS)

