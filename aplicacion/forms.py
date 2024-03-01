from django.forms import ModelForm
from .models import Informe, Usuario, GeneracionEnergia
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
        fields = ['cedula', 'gmail', 'direccion']



from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import password_validation

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        self.fields['password1'].validators.extend([
            self.validate_password_similarity,
            self.validate_common_password,
            self.validate_numeric_password,
        ])

    def validate_password_similarity(self, password):

        pass

    def validate_common_password(self, password):

        pass

    def validate_numeric_password(self, password):

        if password.isdigit():
            raise forms.ValidationError("La contraseña no puede ser completamente numérica.")

    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        try:
            password_validation.validate_password(password, self.instance)
        except forms.ValidationError as error:
            error_messages = list(error.messages)
            error_messages = [msg.replace("contraseña", "clave") for msg in error_messages]
            self.add_error('password1', forms.ValidationError(error_messages))

        return password

    #########

    from django import forms
    from .models import GeneracionEnergia



class GeneracionEnergiaForm(forms.ModelForm):
    class Meta:
        model = GeneracionEnergia
        fields = '__all__'
    pass