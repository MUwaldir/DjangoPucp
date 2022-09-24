from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import usuarioApp
import json

# Create your views here.
def index(request):
    return render(request,'ejemploAjax/index.html')

def cargarInformacion(request,num):
    if num == '1':
        return HttpResponse('Texto 1 del servidor')
    else:
        return HttpResponse('Texto del servidor, no se recibio 1')

def cargarInfoUsuario(request):
    nombre = request.GET.get('nombre')
    apellido = request.GET.get('apellido')
    return JsonResponse({
        'usuario_1' :{
            'nombre':str(nombre),
            'apellido':str(apellido),
            'edad':'25',  
        },
        'usuario_2' :{
            'nombre':'javier',
            'apellido':'hilario',
            'edad':'35',
        }      
    })

def cargarUsuarios(request):
    categoria_usuario = str(request.GET.get('categoria'))
    usuarios_totales = usuarioApp.objects.filter(categoria=categoria_usuario).order_by('id')
    usuarios_info = []
    for usuario in usuarios_totales:
        usuarios_info.append([usuario.id,usuario.nombre,usuario.apellido,usuario.edad,usuario.direccion])
    return JsonResponse({
        'usuarios':usuarios_info,
    })

def guardarUsuario(request):
    informacion = json.load(request)
    nombre = informacion.get('nombre')
    apellido = informacion.get('apellido')
    edad = informacion.get('edad')
    direccion = informacion.get('direccion')
    categoria = informacion.get('categoria')
    print(nombre)
    print(apellido)
    print(edad)
    print(direccion)
    print(categoria)
    return JsonResponse({
        'info':'post aceptado'
    })