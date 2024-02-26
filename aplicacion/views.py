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

def RegistroDispositivos(request):
    if request.method == 'POST':
        form = DispositivoForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = DispositivoForm()
    return render(request, 'RegistroDispositivos.html', {'form': form})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Dispositivo


def GenerarInforme(request):
    dispositivos = Dispositivo.objects.all()

    if request.method == 'POST':
        dispositivo_id = request.POST.get('dispositivo_id')
        dispositivo = get_object_or_404(Dispositivo, pk=dispositivo_id)
        dispositivo.delete()
        return redirect('GenerarInforme')

    return render(request, 'GenerarInforme.html', {'dispositivos': dispositivos})
from aplicacion.models import Dispositivo

def presentacion(request):

    dispositivos = Dispositivo.objects.all()

    context = {'dispositivos': dispositivos}

    return render(request, 'presentacion.html', context)


from django.shortcuts import render, redirect
from .models import Usuario
from .forms import UsuarioForm

def perfil(request):
    usuario_actual = request.user
    perfil_usuario, creado = Usuario.objects.get_or_create(user=usuario_actual)

    # Obtener datos ingresados almacenados en la sesión
    datos_ingresados = request.session.get('datos_ingresados', {})

    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=perfil_usuario)

        if form.is_valid():
            form.save()

            # Actualizar datos ingresados después de guardar el formulario
            datos_ingresados = {
                'Nombre': perfil_usuario.user.username,
                'Cédula': perfil_usuario.cedula,
                'Correo': perfil_usuario.gmail,
                'Dirección': perfil_usuario.direccion,
            }

            # Almacenar los datos en la sesión
            request.session['datos_ingresados'] = datos_ingresados

            return redirect('perfil')  # Redirigir para evitar reenvío del formulario al actualizar la página

    else:
        form = UsuarioForm(instance=perfil_usuario)

    return render(request, 'perfil.html', {'usuario_actual': usuario_actual, 'perfil_usuario': perfil_usuario, 'form': form, 'datos_ingresados': datos_ingresados})

from django.shortcuts import render
from .models import Dispositivo

from itertools import groupby

from itertools import groupby

def Estadisticas(request):
    # Obtén los datos de dispositivos desde tu modelo
    dispositivos = Dispositivo.objects.all()

    # Agrupa los dispositivos por nombre y suma las energías
    dispositivos_agrupados = []
    for key, group in groupby(dispositivos, key=lambda x: x.nombre_dispositivo):
        dispositivos_agrupados.append({
            'nombre_dispositivo': key,
            'total_energia': sum(item.total_energia for item in group),
        })

    # Calcula el dispositivo que más consume
    dispositivo_mas_consumo = max(dispositivos_agrupados, key=lambda x: x['total_energia'], default=None)

    # Convierte los datos a un formato que pueda ser procesado por JavaScript en la plantilla
    dispositivos_json = serialize_dispositivos(dispositivos_agrupados)

    # Pasa los datos a la plantilla
    return render(request, 'Estadisticas.html', {'dispositivos_json': dispositivos_json, 'dispositivo_mas_consumo': dispositivo_mas_consumo})

def serialize_dispositivos(dispositivos):
    # Convierte los datos de dispositivos a un formato JSON
    serialized_dispositivos = []
    for dispositivo in dispositivos:
        serialized_dispositivo = {
            'nombre_dispositivo': dispositivo['nombre_dispositivo'],
            'total_energia': dispositivo['total_energia'],
        }
        serialized_dispositivos.append(serialized_dispositivo)

    return serialized_dispositivos