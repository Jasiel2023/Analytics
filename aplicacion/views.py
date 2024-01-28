from django.shortcuts import render
import Analytics
from aplicacion.models import DISPOSITIVOS
from aplicacion.models import Usuario
from aplicacion.models import registroDispositivos
from aplicacion.models import Informe

from django.forms import ModelForm
from aplicacion.models import Usuario, MedidorDeConsumo, Informe, DISPOSITIVOS,Registro
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
#from .forms import LoginForm

#def user_login(request):
#   if request.methodo == 'POST':
#       form = LoginForm(request.POST)
#       if form.is_valid():
#           cd = form.cleaned_data
#           user = authenticate(request,
#                               username = cd['username'],
#                               password = cd['password']) #NONE
#           if user is not None:
#               if user.is_active:
#                   login(request, user)
#                   return HttpResponse('Usuario autenticado')
 #               else:
#                  return HttpResponse('El usuario no esta activo')
 #           else:
#              return HttpResponse('La informacion no es corecta')
 #   else:
#      form = LoginForm()
#       return render(request, 'login.html', {'form': form})

#@login_required
#def RegistroDeDispositivos(request):
 #   return render(request, 'aplicacion/RegistroDeDispositivos.html')



def index(request):
    return render(request, 'index.html')

def login(request):
    dispositivos = DISPOSITIVOS.objects.all()
    usuario = Usuario.objects.all()
    return render(request, 'login2.html', {'usuario': usuario})

def RegistroDeDispositivos(request):
    dispositivos = DISPOSITIVOS.objects.all()
    return render(request, 'RegistroDeDispositivos.html', {'dispositivos':dispositivos})

def FormularioDeDispositivos(request):
    registro = registroDispositivos.objects.all()
    return render(request, 'FormularioDeDispositivos.html', {'registro': registro})

def GenerarInforme(request):
    informe = Informe.objects.all()
    return render(request, 'GenerarInforme.html', {'informe':informe})

def registro(request):
   registro = Usuario.objects.all()
   return render(request, 'registro.html', {'registro':registro})

def inicio(request):
    return render(request, 'inicio.html')

