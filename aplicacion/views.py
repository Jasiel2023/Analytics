
from aplicacion.models import registroDispositivos
from .forms import InformeForm

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

###

from . forms import DispositivoForm

def formulario(request):
    if request.method == 'POST':
        form = DispositivoForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = DispositivoForm()
    return render(request, 'formulario.html', {'form': form})

def GenerarInforme(request):
    dispositivos = Dispositivo.objects.all()
    return render(request, 'GenerarInforme.html', {'dispositivos': dispositivos})

from aplicacion.models import Dispositivo

def presentacion(request):

    dispositivos = Dispositivo.objects.all()

    context = {'dispositivos': dispositivos}

    return render(request, 'presentacion.html', context)


from django.shortcuts import render, redirect
from .forms import UsuarioForm
from django.contrib.auth.decorators import login_required
from .models import Usuario

@login_required
def perfil(request):
    usuario_actual = request.user
    perfil_usuario, creado = Usuario.objects.get_or_create(user=usuario_actual)

    if request.method == 'POST':
        form = UsuarioForm(request.POST)

        if form.is_valid():
            perfil_usuario.cedula = form.cleaned_data['cedula']
            perfil_usuario.gmail = form.cleaned_data['gmail']
            perfil_usuario.api_google_maps = form.cleaned_data['api_google_maps']
            perfil_usuario.save()

            return redirect('perfil.html')

    else:

        form = UsuarioForm()

    return render(request, 'perfil.html', {'usuario_actual': usuario_actual, 'perfil_usuario': perfil_usuario, 'form': form})