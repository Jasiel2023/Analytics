from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from . forms import DispositivoForm
from django.shortcuts import redirect
from .models import Dispositivo
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Usuario
from .forms import UsuarioForm
from itertools import groupby

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


def RegistroDispositivos(request):
    if request.method == 'POST':
        form = DispositivoForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = DispositivoForm()
    return render(request, 'RegistroDispositivos.html', {'form': form})

def GenerarInforme(request):
    dispositivos = Dispositivo.objects.all()

    if request.method == 'POST':
        dispositivo_id = request.POST.get('dispositivo_id')
        dispositivo = get_object_or_404(Dispositivo, pk=dispositivo_id)
        dispositivo.delete()
        return redirect('GenerarInforme')

    return render(request, 'GenerarInforme.html', {'dispositivos': dispositivos})


def presentacion(request):

    dispositivos = Dispositivo.objects.all()

    context = {'dispositivos': dispositivos}

    return render(request, 'presentacion.html', context)

def perfil(request):

    usuario_instance, created = Usuario.objects.get_or_create(user=request.user)
    has_perfil = created

    if request.method == 'POST':
        perfil_form = UsuarioForm(request.POST, instance=usuario_instance)
        if perfil_form.is_valid():
            perfil_form.save()
            return HttpResponseRedirect('/')
    else:
        perfil_form = UsuarioForm(instance=usuario_instance)

    return render(request, 'perfil.html', {'perfil_form': perfil_form, 'has_perfil': has_perfil})

def editar_perfil(request, user_id):
    usuario = get_object_or_404(User, id=user_id)
    usuario_instance = get_object_or_404(Usuario, user=usuario)

    if request.method == 'POST':
        perfil_form = UsuarioForm(request.POST, instance=usuario_instance)
        if perfil_form.is_valid():
            perfil_form.save()
            return HttpResponseRedirect('/')
    else:
        perfil_form = UsuarioForm(instance=usuario_instance)

    return render(request, 'perfil.html', {'perfil_form': perfil_form, 'has_perfil': True})
def Estadisticas(request):

    dispositivos = Dispositivo.objects.all().order_by('nombre_dispositivo')

    dispositivos_agrupados = []
    for key, group in groupby(dispositivos, key=lambda x: x.nombre_dispositivo):
        dispositivos_agrupados.append({
            'nombre_dispositivo': key,
            'total_energia': sum(item.total_energia for item in group),
        })

    dispositivo_mas_consumo = max(dispositivos_agrupados, key=lambda x: x['total_energia'], default=None)

    dispositivos_json = serialize_dispositivos(dispositivos_agrupados)


    return render(request, 'Estadisticas.html', {'dispositivos_json': dispositivos_json, 'dispositivo_mas_consumo': dispositivo_mas_consumo})
def serialize_dispositivos(dispositivos):

    serialized_dispositivos = []
    for dispositivo in dispositivos:
        serialized_dispositivo = {
            'nombre_dispositivo': dispositivo['nombre_dispositivo'],
            'total_energia': dispositivo['total_energia'],
        }
        serialized_dispositivos.append(serialized_dispositivo)

    return serialized_dispositivos



