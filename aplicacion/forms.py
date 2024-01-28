from django.forms import ModelForm
from .models import Informe
class InformeForm(ModelForm):
    class meta:
        model = Informe
        fields = ['fechaAnalisis']
