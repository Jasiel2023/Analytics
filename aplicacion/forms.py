from django.forms import ModelForm
from .models import Informe, Usuario
from django import forms
from . models import Dispositivo

class InformeForm(ModelForm):
    class meta:
        model = Informe
        fields = ['fechaAnalisis']

class DispositivoForm(forms.ModelForm):
    class Meta:
        model = Dispositivo
        fields = '__all__'
class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'


