from django.forms import ModelForm
from .models import Informe, Usuario


class InformeForm(ModelForm):
    class meta:
        model = Informe
        fields = ['fechaAnalisis']

###

from django import forms
from . models import Dispositivo

class DispositivoForm(forms.ModelForm):
    class Meta:
        model = Dispositivo
        fields = '__all__'
class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
from django import forms

