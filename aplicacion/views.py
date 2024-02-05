from django.shortcuts import render, redirect
import Analytics
#from aplicacion.models import DISPOSITIVOS
from aplicacion.models import Usuario
from aplicacion.models import registroDispositivos
from aplicacion.models import Informe
from .forms import InformeForm

from django.forms import ModelForm
from aplicacion.models import Usuario, MedidorDeConsumo, Informe,Registro
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
def index(request):
    return render(request, 'index.html')

def registro(request):
    if request.method == 'GET':
        return render(request, 'registro.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],
                                                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('presentacion')
            except IntegrityError:
                return render(request, 'registro.html', {'form': UserCreationForm,
                                              "error": 'Username ya existe'})
        return render(request, 'registro.html', {'form': UserCreationForm,
                                                 "error": 'Contraseña no coincide'})


def RegistroDeDispositivos(request):
    #dispositivos = DISPOSITIVOS.objects.all()
    return render(request, 'RegistroDeDispositivos.html')

def FormularioDeDispositivos(request):
    registro = registroDispositivos.objects.all()
    return render(request, 'FormularioDeDispositivos.html', {'registro': registro})

def GenerarInforme(request):
    return render(request, 'GenerarInforme.html', {
        'form' : InformeForm })


def inicio(request):#ojo a esto
    return render(request, 'inicio.html')

def presentacion(request):
    return render(request, 'presentacion.html')

def cerrarSesion(request):
    logout(request)
    return redirect('iniciarSesion')

def iniciarSesion(request):
    if request.method == 'GET':
         return render(request, 'iniciarSesion.html',
                  {'form': AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'],
                     password=request.POST['password'])
        if user is None:
            return render(request, 'iniciarSesion.html',
                          {'form': AuthenticationForm,
                           'error': 'Usuario o contraseña es incorrecta'})
        else:
            login(request, user)
            return redirect('presentacion')